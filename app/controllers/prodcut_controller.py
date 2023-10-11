from flask_restful import Resource

from app.services.product_service import ProductService


class ProductController(Resource):
    def __init__(self):
        self.product_service = ProductService()

    def get_product(self, id_type: int = None, id_num: int = None):
        if id_type != None and id_num != None:
            return self.product_service.get_by_id(id_type=id_type, id_num=id_num)
        return None
