from flask import Flask
from flask_graphql import GraphQLView

# Config stuff
from config import App

# Tools
from tools.config_sentry import init_sentry

# Routes
from routes.stats import stats

# Database
from db.config import connect_db
from db.schema.schema import schema


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    # Connect/prep database stuff and attach it to the app instance
    # TODO: Wrap in error handling
    app.db = connect_db(config["mongo_config"])

    # Basic non-graphql routes
    app.register_blueprint(stats)

    # graphql setup
    use_graphiql = config['IS_DEV']
    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql', schema=schema, graphiql=use_graphiql)
    )

    # if config['FLASK_ENV'] != 'production':
    #     # Configure tools like Sentry for monitoring the app
    # TODO: Move this to production once you actually deploy
    init_sentry(config['sentry_config'])

    return app


if __name__ == "__main__":
    app = create_app(App.get_all())
    app.run(host=App.config('HOST'))
