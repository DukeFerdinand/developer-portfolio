import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration


def init_sentry(sentry_config):
    sentry_sdk.init(
        dsn=sentry_config["SENTRY_DSN"],
        release=sentry_config["RELEASE"],
        integrations=[FlaskIntegration()]
    )
