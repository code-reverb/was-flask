from .utils import config
from flask import Flask, Blueprint
from flask_restx import Api
from code_reverb.routes import add_namespaces


blueprint = Blueprint("api", __name__)


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    api = Api(
        blueprint,
        title="CODE Reverb WEB APPLICATION",
        description="code reverb web service with flask restx apis",
    )

    add_namespaces(api)

    return app
