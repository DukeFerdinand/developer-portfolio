from flask import Flask

# Config stuff
from config import App
from db.config import connect_db

# Tools
from tools.config_sentry import init_sentry

# Routes
from routes.stats import stats


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    # Connect/prep database stuff and attach it to the app instance
    # TODO: Wrap in error handling
    app.db = connect_db(config["mongo_config"])

    # Basic non-data routes
    app.register_blueprint(stats)

    # if config['FLASK_ENV'] != 'production':
    #     # Configure tools like Sentry for monitoring the app
    # TODO: Move this to production once you actually deploy
    init_sentry(config['sentry_config'])

    return app


if __name__ == "__main__":
    app = create_app(App.get_all())
    app.run(host=App.config('HOST'))
