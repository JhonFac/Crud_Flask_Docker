import unittest
from unittest.mock import Mock, patch

import mock
import requests
from flask import Flask, Response, json

from app import create_app
from app.controllers.customer_controller import CustomerController


class TestCustomerRoutes(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.controller = CustomerController()
        self.mock_db = Mock()
        self.app = create_app()
        self.url_product = f"http://localhost:5000/{self.app.config.get('VERSION')}/product/client/basicInfo"
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()
        with open("./tests/customer_data.json", "r") as file:
            self.json_data = json.load(file)
        self.headers = {
            "X-CustIdentNum": "12345678",
            "X-CustIdentType": "1",
            "X-IPAddr": "192.87.2.34",
            "X-Name": "Cobranzas",
            "X-RqUID": "be585a4e-1ebb-4c10-8336-1110333bfab5",
            "X-Channel": "SuperApp",
        }

    @mock.patch("app.routes.routes.CustomerController.get_client")
    def test_get_client_with_mock_decorator(self, mock_get_client):
        self.controller.get_client.return_value = Response(
            response=json.dumps(self.json_data), status=200, content_type="application/json"
        )
        response = self.controller.get_client(type_id=1, custom_id=123)
        self.assertEqual(json.loads(response.data), self.json_data)
        self.assertEqual(response.status_code, 200)

    def test_get_customer_invalid_headers(self):
        self.headers.pop("X-CustIdentNum")
        response = self.client.get(self.url_product, headers=self.headers)

        self.assertEqual(response.status_code, 400)

    @patch("app.controllers.customer_controller.CustomerController.get_client")
    def test_get_customer_is_empty(self, mock_get_client):
        mock_get_client.return_value = Response(response=None, status=204)
        response = self.controller.get_client(type_id=1, custom_id=123)
        self.assertEqual(response.status_code, 204)

    def test_get_customer_server_error(self):
        self.app.config[
            "SQLALCHEMY_DATABASE_URI"
        ] = "postgresql://postgres:PpvBmpx5tMA1mmkHlvPs@containers-us-west-91.railway.app:7825/railwa"
        response = self.client.get(self.url_product, headers=self.headers)
        self.assertEqual(response.status_code, 500)
