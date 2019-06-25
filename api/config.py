from os import environ


class App:
    __conf = {
        "FLASK_ENV": environ["FLASK_ENV"] or "production",
        "IS_DEV": environ["IS_DEV"] or False,
        "HOST": environ["HOST"] or "127.0.0.1",
        "sentry_config": {
            "SENTRY_DSN": environ["SENTRY_DSN"] or "",
            "RELEASE": environ["RELEASE"]
        },
        "mongo_config": {
            "MONGO_DB": environ["MONGO_DB"],
            "MONGO_HOST": environ["MONGO_HOST"],
            "MONGO_USR": environ["MONGO_USR"],
            "MONGO_PWD": environ["MONGO_PWD"],
            "MONGO_PORT": environ["MONGO_PORT"]
        }
    }

    @staticmethod
    def config(env_var):
        return App.__conf[env_var]

    @staticmethod
    def get_all():
        return App.__conf
