from flask import Blueprint, jsonify
from flask import current_app as app
from zaifbot.errors import InvalidRequest

resource = Blueprint('strategies', __name__, url_prefix='/strategies')


@resource.route('/', methods=['GET'])
def index():
    res = jsonify(app.portfolio.index())
    return res


@resource.route('/', methods=['POST'])
def create():
    pass


@resource.route('/<id_>', methods=['GET'])
def show(id_):
    strategy = app.portfolio.find_strategy(id_)
    if strategy:
        res = jsonify(strategy.get_info())
        return res
    raise InvalidRequest('strategy not found', status_code=404)


@resource.route('/<id_>', methods=['DELETE'])
def stop(id_):
    strategy = app.portfolio.find_strategy(id_)
    if strategy is None:
        raise InvalidRequest('strategy not found', status_code=404)


@resource.route('/<id_>/suspend', methods=['PATCH'])
def suspend(id_):
    pass
