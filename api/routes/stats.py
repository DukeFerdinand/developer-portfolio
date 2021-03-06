from flask import Blueprint, current_app, jsonify

from tools.utils import debug

stats = Blueprint("stats", __name__)


@stats.route('/')
def health_check():
    return jsonify({"msg": "API OK"})


@stats.route('/db-health-check')
def db_health_check():
    db = current_app.db
    res = db.test.find_one()['content']
    return res
