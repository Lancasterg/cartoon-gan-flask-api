import unittest

from flask_api.app_resources import ModelEndpointResource, PaprikaEndpoint, ShinkaiEndpoint


class TestModelResource(unittest.TestCase):

    mer = ModelEndpointResource()

    def test_endpoint(self):
        self.assertEqual(self.mer.get_endpoint(), "super_endpoint")

    def test_style(self):
        self.assertEqual(self.mer.get_style(), "super_style")


class TestPaprikaEndpoint(unittest.TestCase):

    paprika_endpoint = PaprikaEndpoint()

    def test_endpoint(self):
        self.assertEqual(self.paprika_endpoint.get_endpoint(), "/v1/paprika")

    def test_style(self):
        self.assertEqual(self.paprika_endpoint.get_style(), "paprika")


class TestShinkaiEndpoint(unittest.TestCase):
    paprika_endpoint = ShinkaiEndpoint()

    def test_endpoint(self):
        self.assertEqual(self.paprika_endpoint.get_endpoint(), "/v1/shinkai")

    def test_style(self):
        self.assertEqual(self.paprika_endpoint.get_style(), "shinkai")
