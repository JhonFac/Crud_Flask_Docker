from app.models.product_model import ProductCustomerModel


class ProductService:
    def __init__(self):
        self.productModel = ProductCustomerModel()

    def get_by_id(self, id_type: int, id_num: int):
        return self.productModel.get_by_id(id_type, id_num, many=True)
