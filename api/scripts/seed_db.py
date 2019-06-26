from os import environ, path
from sys import argv
from json import load
from pprint import PrettyPrinter

from pymongo import MongoClient

pp = PrettyPrinter(indent=2)


c = {
    "MONGO_DB": environ["MONGO_DB"],
    "MONGO_HOST": environ["MONGO_HOST"],
    "MONGO_USR": environ["MONGO_USR"],
    "MONGO_PWD": environ["MONGO_PWD"],
    "MONGO_PORT": environ["MONGO_PORT"]
}

database_connection = MongoClient(
    f"mongodb://{c['MONGO_USR']}:{c['MONGO_PWD']}@{c['MONGO_HOST']}:{c['MONGO_PORT']}")['dev-portfolio']


collections = {}
with open(path.join(path.dirname(__file__), 'dev-portfolio.json')) as file:
    collections = load(file)


class DBController:
    def __init__(self, db, data):
        self.db = db
        # Selected Collection
        self.sc = ''
        self.data = data

    def up(self, auto_run):
        if not auto_run:
            run_seed = input(
                'Warning, running UP on a live database can have disastrous effects, continue? [y/N]: ')
        if auto_run or run_seed.lower() == 'y':
            self.down(auto_run)
            for collection in self.data:
                print(f'Reached collection {collection}')
                self.sc = self.db[collection]
                for doc in self.data[collection]:
                    print('> Inserting doc:')
                    pp.pprint(doc)
                    self.sc.insert_one(doc)
                    print('> Done')
            print('Done. Database is seeded!')
        else:
            print('Aborting')

    def down(self, auto_run):
        if not auto_run:
            run_seed = input(
                'Warning, running UP on a live database can have disastrous effects, continue? [y/N]: ')
        if auto_run or run_seed.lower() == 'y':
            for collection in collections:
                print(f'> Taking down collection {collection}')
                self.db[collection].drop()
                print('Collection droppped.')
            print('Done. Database is cleared')


if (argv[1] == "up"):
    db = DBController(database_connection, collections)
    try:
        auto_run = argv[2]
        db.up((auto_run == '-y'))
    except IndexError:
        db.up(False)
elif (argv[1] == "down"):
    db = DBController(database_connection, collections)
    try:
        auto_run = argv[2]
        db.down((auto_run == '-y'))
    except IndexError:
        db.down(False)
