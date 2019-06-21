from flask import Blueprint

stats = Blueprint("stats", __name__)


@stats.route('/')
def health_check():
    return 'API OK'
