import unittest
from unittest.mock import MagicMock

from app.controllers.prodcut_controller import ProductController
from app.models.product_model import ProductCustomerModel


class ProductControllerTest(unittest.TestCase):
    def setUp(self):
        self.controller = ProductController()
        self.product_service = MagicMock()
        self.controller.product_service = self.product_service

    def test_get_product_with_invalid_parameters(self):
        result = self.controller.get_product(None, 42)
        assert result == None

    def test_get_product_with_valid_parameters(self):
        expected_result = ProductCustomerModel()
        self.product_service.get_by_id.return_value = expected_result
        result = self.controller.get_product(2, 12345679)
        self.assertEqual(result, expected_result)
