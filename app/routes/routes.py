from flask import Blueprint, abort, request
from flask_restful import Resource

from app.controllers.customer_controller import CustomerController
from app.controllers.prodcut_controller import ProductController
from app.routes.headers import headers_required, require_headers
from app.schemas.client_schema import ClientSchema
from app.schemas.product_schema import ProductDataSchema
from app.utils.response import error_response, success_response

bp = Blueprint("v1", __name__, url_prefix="/v1/product/client/")

customer_schema = ClientSchema()
product_schema = ProductDataSchema()

customer_controller = CustomerController()
product_controller = ProductController()


def set_routes(app):
    app.register_blueprint(bp)


@bp.route("/basicInfo", methods=["GET"])
@require_headers(headers_required)
def get_customer_data():
    custom_id = request.headers.get("X-CustIdentNum")
    type_id = request.headers.get("X-CustIdentType")
    data = customer_controller.get_client(type_id, custom_id)
    if data:
        return success_response(customer_schema.dump(data))
    return error_response("", 204)


@bp.route("/product", methods=["GET"])
@require_headers(headers_required)
def get_product():
    custom_id = request.headers.get("X-CustIdentNum")
    type_id = request.headers.get("X-CustIdentType")
    data = product_controller.get_product(id_type=type_id, id_num=custom_id)
    if data:
        return success_response(product_schema.dump(data, many=True))
    return error_response("", 204)
