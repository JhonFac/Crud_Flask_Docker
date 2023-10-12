from flask import Blueprint, abort, request
from flask_restful import Resource

from app.controllers.customer_controller import CustomerController
from app.controllers.prodcut_controller import ProductController
from app.routes.headers import headers_required, require_headers
from app.schemas.client_schema import ClientSchema
from app.schemas.product_schema import ProductDataSchema
from app.utils.response import error_response, success_response

bp = Blueprint("v1", __name__, url_prefix="/v1/product/client/")

customerSchema = ClientSchema()
productSchema = ProductDataSchema()

customer_controller = CustomerController()
product_controller = ProductController()
example_schema = ClientSchema()


def set_routes(app):
    app.register_blueprint(bp)


@bp.route("/basicInfo", methods=["GET"])
@require_headers(headers_required)
def get_customer_data():
    customId = request.headers.get("X-CustIdentNum")
    typeId = request.headers.get("X-CustIdentType")
    data = customer_controller.get_client(typeId, customId)
    if data:
        return success_response(customerSchema.dump(data))
    return error_response("", 204)


@bp.route("/product", methods=["GET"])
@require_headers(headers_required)
def get_product():
    customId = request.headers.get("X-CustIdentNum")
    typeId = request.headers.get("X-CustIdentType")
    data = product_controller.get_product(id_type=typeId, id_num=customId)
    if data:
        return success_response(productSchema.dump(data, many=True))
    return error_response("", 204)
