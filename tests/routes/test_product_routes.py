import unittest

import requests
from flask import Flask, json

from app import create_app


class TestProductRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.url_product = f"http://localhost:5000/{self.app.config.get('VERSION')}/product/client/product"
        self.app.config["TESTING"] = True
        self.product = self.app.test_client()
        self.headers = {
            "X-CustIdentNum": "12345679",
            "X-CustIdentType": "2",
            "X-IPAddr": "192.87.2.34",
            "X-Name": "Cobranzas",
            "X-RqUID": "be585a4e-1ebb-4c10-8336-1110333bfab5",
            "X-Channel": "SuperApp",
        }

    def test_get_customer_data(self):
        response = self.product.get(self.url_product, headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_get_customer_invalid_headers(self):
        self.headers.pop("X-CustIdentNum")
        response = self.product.get(self.url_product, headers=self.headers)
        self.assertEqual(response.status_code, 400)

    def test_get_customer_is_empty(self):
        self.headers["X-CustIdentType"] = 6
        response = self.product.get(self.url_product, headers=self.headers)
        self.assertEqual(response.status_code, 204)

    def test_get_customer_server_error(self):
        self.app.config[
            "SQLALCHEMY_DATABASE_URI"
        ] = "postgresql://postgres:PpvBmpx5tMA1mmkHlvPs@containers-us-west-91.railway.app:7825/railwa"
        response = self.product.get(self.url_product, headers=self.headers)
        self.assertEqual(response.status_code, 500)
