from flask import Flask
from fizzbuzz.ext import configuration
import logging

logger = logging.getLogger(__name__)


def minimal_app(**config) -> Flask:
    app = Flask(__name__)
    configuration.init_app(app, **config)
    return app


def create_app(**config) -> Flask:
    """
    Creates an application instance to run
    :return: A Flask object
    """

    app = minimal_app(**config)
    app.config["SECRET_KEY"] = "7e1b447b-568d-445f-bf68-b80d35d9d3fb"
    configuration.load_extensions(app)
    return app
