from os import environ, path
from sys import argv
from json import load

from db.config import connect_db
from db.models.models import Page, PageData


c = {
    "MONGO_DB": environ["MONGO_DB"],
    "MONGO_HOST": environ["MONGO_HOST"],
    "MONGO_USR": environ["MONGO_USR"],
    "MONGO_PWD": environ["MONGO_PWD"],
    "MONGO_PORT": environ["MONGO_PORT"]
}

collections = {}
with open(path.join(path.dirname(__file__), 'dev-portfolio.json')) as file:
    collections = load(file)

db = connect_db(c)


def confirm_choice(choice):
    return input(f'Warning! Running "{choice}" on the database will DESTROY everything. Proceed? [y/N] ').lower() == 'y'


# TODO: Dump the data into the seed when you're done with dev
if argv[1] == "up":
    if confirm_choice('up'):
        db.drop_database(c['MONGO_DB'])
        page = Page(
            page_type="front_page",
            page_data=PageData(page_title="Doug Flynn")
        )
        page.save()
    else:
        print('Aborting')
elif argv[1] == "down":
    if confirm_choice('down'):
        print(c['MONGO_DB'])
        db.drop_database(c['MONGO_DB'])
    else:
        print('Aborting')
