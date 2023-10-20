import unittest
from unittest.mock import Mock, patch

import mock
from flask import Response, json

from app import create_app
from app.controllers.prodcut_controller import ProductController


class TestProductRoutes(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.controller = ProductController()
        self.mock_db = Mock()
        self.app = create_app()
        self.url_product = f"http://localhost:5000/{self.app.config.get('VERSION')}/product/client/product"
        self.app.config["TESTING"] = True
        self.product = self.app.test_client()
        with open("./tests/product_data.json", "r") as file:
            self.json_data = json.load(file)
        self.headers = {
            "X-CustIdentNum": "12345679",
            "X-CustIdentType": "2",
            "X-IPAddr": "192.87.2.34",
            "X-Name": "Cobranzas",
            "X-RqUID": "be585a4e-1ebb-4c10-8336-1110333bfab5",
            "X-Channel": "SuperApp",
        }

    @mock.patch("app.routes.routes.ProductController.get_product")
    def test_get_product_with_mock_decorator(self, mock_get_product):
        self.controller.get_product.return_value = Response(
            response=json.dumps(self.json_data), status=200, content_type="application/json"
        )
        response = self.controller.get_product(type_id=1, custom_id=123)
        self.assertEqual(json.loads(response.data), self.json_data)
        self.assertEqual(response.status_code, 200)

    def test_get_customer_invalid_headers(self):
        self.headers.pop("X-CustIdentNum")
        response = self.product.get(self.url_product, headers=self.headers)
        self.assertEqual(response.status_code, 400)

    @patch("app.controllers.prodcut_controller.ProductController.get_product")
    def test_get_customer_is_empty(self, mock_get_product):
        mock_get_product.return_value = Response(response=None, status=204)
        response = self.controller.get_product(type_id=1, custom_id=123)
        self.assertEqual(response.status_code, 204)

    def test_get_customer_server_error(self):
        self.app.config[
            "SQLALCHEMY_DATABASE_URI"
        ] = "postgresql://postgres:PpvBmpx5tMA1mmkHlvPs@containers-us-west-91.railway.app:7825/railwa"
        response = self.product.get(self.url_product, headers=self.headers)
        self.assertEqual(response.status_code, 500)
