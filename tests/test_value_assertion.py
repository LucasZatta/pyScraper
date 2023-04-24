import unittest
from app import app
from unittest.mock import patch
from flask import url_for
import api.routes

class TestInputValidation(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    @patch('api.routes.get_url')
    def test_endpoint(self, mock_get_url):
        with app.test_request_context('/scrape?url=foo'): 
            response = api.routes.get_url_info()
        self.assertEqual(response.status_code, 400)

        with app.test_request_context('/scrape?url=foo.com'): 
            mock_get_url.return_value = ""
            response = api.routes.get_url_info()
        self.assertEqual(response.status_code, 200)

        
        # response = self.client.get("/scrape?url=www.google.com")
        # self.assertEqual(response.thestatus_code, 200)