from flask import Flask
from . import models
from . import routes


def create():
    app = Flask(__name__)

    app.register_blueprint(routes.endpoints)

    session = _make_session()
    app.session = session

    return app


def _make_session():
    engine = models.sqlite_engine()
    return models.get_session(engine)
