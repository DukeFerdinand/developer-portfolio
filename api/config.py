from os import environ


class App:
    __conf = {
        "FLASK_ENV": environ["FLASK_ENV"] or "production",
        "IS_DEV": environ["IS_DEV"] or False,
        "HOST": environ["HOST"] or "127.0.0.1",
        "sentry_config": {
            "SENTRY_DSN": environ["SENTRY_DSN"] or "",
            "RELEASE": environ["RELEASE"]
        }
    }

    @staticmethod
    def config(env_var):
        return App.__conf[env_var]

    @staticmethod
    def get_all():
        return App.__conf
