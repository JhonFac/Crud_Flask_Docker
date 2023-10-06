from flask import Blueprint, abort, request

from app.controllers.controller import Controller
from app.routes.headers import headers_required, require_headers
from app.schemas.client_schema import ClientSchema

bp = Blueprint("v1", __name__, url_prefix="/v1/product/client/")
controller = Controller()
example_schema = ClientSchema()


def set_routes(app):
    app.register_blueprint(bp)


@bp.route("/basicInfo", methods=["GET"])
@require_headers(headers_required)
def get_all_examples():
    customId = request.headers.get("X-CustIdentNum")
    typeId = request.headers.get("X-CustIdentType")
    return controller.get(typeId, customId)


@bp.route("/basicInfo", methods=["POST"])
def create():
    return controller.post(request.get_json())


@bp.route("/basicInfo", methods=["DELETE"])
def delete():
    return controller.delete(request.get_json())
