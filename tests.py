import unittest
from unittest import TestCase
from server import app
from model import connect_to_db, db, example_data

# class BasicPagesIntegrationTest(TestCase):
#     """Some smoke tests."""

#     def setUp(self):
#         tc = app.test_client()
#         self.client = tc

#     def test_homepage(self):
#         resp = self.client.get("/")
#         self.assertIn("OMG", resp.data)
#         self.assertIn("CARS", resp.data)

#     def test_brands_page(self):
#         # make request to /brands route
#         resp = self.client.get("/brands/all")
#         self.assertEqual(200, resp.status_code)
#         self.assertNotEqual(404, resp.status_code)
#         self.assertIn("All Brands", resp.data)

#     def test_models_page(self):
#         resp = self.client.get("/models/all")
#         self.assertEqual(200, resp.status_code)
#         self.assertNotEqual(404, resp.status_code)
#         self.assertIn("All Models", resp.data)

class DatabaseIntegrationTest(TestCase):
    def setUp(self):

        connect_to_db(app, "postgresql:///testdb")

        db.create_all()
        example_data()

        self.client = app.test_client()

    def test_models_page(self):
        resp = self.client.get("/models/all")
        self.assertIn("2017 Codette", resp.data)
        self.assertIn("3012 Kamry", resp.data)
        self.assertNotIn("2009 Camry", resp.data)

    def tearDown(self):
        db.session.close()
        db.drop_all()
        

if __name__ == "__main__":
    unittest.main()
