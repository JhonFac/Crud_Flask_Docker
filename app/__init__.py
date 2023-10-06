import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.routes.routes import set_routes
from app.utils.response import register_error_handlers

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("app.config.Config")
    register_error_handlers(app)
    set_routes(app)
    return app


# def create_app(config_name):
#     app = Flask(__name__)
#     app.config.from_object(config_name)

#     db.init_app(app)

#     with app.app_context():
#         db.create_all()

#     return app
