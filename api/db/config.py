from mongoengine import connect


def connect_db(c):
    """
    connect_db(config)

    Creates mongo host string from config and attempts connection
    """

    print('Connecting to DB...')

    client = connect(
        host=f"mongodb://{c['MONGO_USR']}:{c['MONGO_PWD']}@{c['MONGO_HOST']}:{c['MONGO_PORT']}")

    print(client)

    db = client[c['MONGO_DB']]

    print("DB connection successful")

    return db
