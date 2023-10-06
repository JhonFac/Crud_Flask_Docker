from flask import Blueprint

from .routes import set_routes as set_example_routes


def set_routes(app):
    example_bp = Blueprint("example", __name__, url_prefix="/example")
    set_example_routes(example_bp)
    app.register_blueprint(example_bp)
