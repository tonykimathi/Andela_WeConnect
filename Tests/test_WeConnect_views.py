import unittest
import json
from app.views import app


class EndpointsTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(self)

    def test_home_route(self):
        response = self.client.get("/", content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_successful_registration(self):
        response = self.client.post("/api/v1/auth/register",
                                    data=json.dumps(dict(username="tim45", email="timmputhia45@email.com",
                                                         password="Password234*", confirm_password="Password234*")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_already_registered(self):
        self.client.post("/api/v1/auth/register",
                         data=json.dumps(dict(username="tony", email="tonymputhia@email.com",
                                              password="Password1*", confirm_password="Password1*")),
                         content_type="application/json")
        response = self.client.post("/api/v1/auth/register",
                                    data=json.dumps(dict(username="tony", email="tonymputhia@email.com",
                                                         password="Password1*", confirm_password="Password1*")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 403)

    def test_successful_login(self):
        self.client.post("/api/v1/auth/register",
                         data=json.dumps(dict(username="tony", email="tonymputhia@email.com",
                                              password="Password1*", confirm_password="Password1*")),
                         content_type="application/json")
        response = self.client.post("/api/v1/auth/login",
                                    data=json.dumps(dict(email="tonymputhia@email.com",
                                                         password="Password1*")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_failed_login(self):
        self.client.post("/api/v1/auth/register",
                         data=json.dumps(dict(username="tony", email="tonymputhia@email.com",
                                              password="Password1*", confirm_password="Password1*")),
                         content_type="application/json")
        response = self.client.post("/api/v1/auth/login",
                                    data=json.dumps(dict(email="tonymputhia@email.com",
                                                         password="Password1*1")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 401)

    def test_successful_logout(self):
        self.client.post("/api/v1/auth/register",
                         data=json.dumps(dict(username="tony", email="tonymputhia@email.com",
                                              password="Password1*", confirm_password="Password1*")),
                         content_type="application/json")
        self.client.post("/api/v1/auth/login",
                         data=json.dumps(dict(email="tonymputhia@email.com",
                                              password="Password1*")),
                         content_type="application/json")
        response = self.client.post("/api/v1/auth/logout", content_type="application/json")

        self.assertEqual(response.status_code, 200)

    def test_reset_password(self):
        self.client.post("/api/v1/auth/reset-password",
                         data=json.dumps(dict(email="timmputhia45@email.com",
                                              new_password="Password234*", confirm_new_password="Password234*")),
                         content_type="application/json")
        response = self.client.post("/api/v1/auth/reset-password",
                                    data=json.dumps(dict(email="timmputhia45@email.com",
                                                         new_password="Password2345*",
                                                         confirm_new_password="Password2345*")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_create_business(self):
        self.client.post("/api/v1/auth/register",
                         data=json.dumps(dict(username="tony", email="tonymputhia@email.com",
                                              password="Password1*", confirm_password="Password1*")),
                         content_type="application/json")
        self.client.post("/api/v1/auth/login",
                         data=json.dumps(dict(email="tonymputhia@email.com",
                                              password="Password1*")),
                         content_type="application/json")
        data = {"owner": "timmputhia@email.com", "business_name": "Jackso 5 Academy",
                "description": "This is a music school established in 1876", "location": "Mississippi",
                "category": "Music School"}
        response = self.client.post("/v1/api/businesses",
                                    data=json.dumps(data),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_update_business_profile(self):
        self.client.post("/api/v1/auth/register",
                         data=json.dumps(dict(username="tony", email="tonymputhia@email.com",
                                              password="Password1*", confirm_password="Password1*")),
                         content_type="application/json")
        self.client.post("/api/v1/auth/login",
                         data=json.dumps(dict(email="tonymputhia@email.com",
                                              password="Password1*")),
                         content_type="application/json")

        data2 = {"owner": "timmputhia@email.com", "business_name": "Jackson 6 Academy",
                 "description": "This is a music school established in 1886", "location": "Mississippi",
                 "category": "Music School"}
        response = self.client.put("/v1/api/businesses/2",
                                   data=json.dumps(data2),
                                   content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_failed_update_business_profile(self):
        self.client.post("/api/v1/auth/register",
                         data=json.dumps(dict(username="tony", email="tonymputhia@email.com",
                                              password="Password1*", confirm_password="Password1*")),
                         content_type="application/json")
        self.client.post("/api/v1/auth/login",
                         data=json.dumps(dict(email="tonymputhia@email.com",
                                              password="Password1*")),
                         content_type="application/json")
        self.client.post("/v1/api/businesses",
                         data=json.dumps(dict(owner="tonymputhia@email.com",
                                              business_name="St. Pius X Academy",
                                              description="This is a primary school established in 2015",
                                              location="Meru County",
                                              category="School")),
                         content_type="application/json")
        response = self.client.put("/v1/api/businesses/4",
                                   data=json.dumps(dict(owner="tonymputhia@email.com",
                                                        business_name="Gilgil Hills Academy",
                                                        description="This is a secondary school established in 2015",
                                                        location="Lodwar County",
                                                        category="School")),
                                   content_type="application/json")
        self.assertEqual(response.status_code, 403)

    def test_delete_business_profile(self):
        self.client.post("/api/v1/auth/register",
                         data=json.dumps(dict(username="tony", email="tonymputhia@email.com",
                                              password="Password1*", confirm_password="Password1*")),
                         content_type="application/json")
        self.client.post("/api/v1/auth/login",
                         data=json.dumps(dict(email="tonymputhia@email.com",
                                              password="Password1*")),
                         content_type="application/json")
        self.client.post("/v1/api/businesses",
                         data=json.dumps(dict(owner="tonymputhia@email.com",
                                              business_name="St. Pius X Academy",
                                              description="This is a primary school established in 2015",
                                              location="Meru County",
                                              category="School")),
                         content_type="application/json")
        response = self.client.delete("/v1/api/businesses/1",
                                      data=json.dumps(dict(owner="tonymputhia@email.com")),
                                      content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_view_businesses(self):
        self.client.post("/api/v1/auth/register",
                         data=json.dumps(dict(username="tony", email="tonymputhia@email.com",
                                              password="Password1*", confirm_password="Password1*")),
                         content_type="application/json")
        self.client.post("/api/v1/auth/login",
                         data=json.dumps(dict(email="tonymputhia@email.com",
                                              password="Password1*")),
                         content_type="application/json")
        self.client.post("/v1/api/businesses",
                         data=json.dumps(dict(owner="tonymputhia@email.com",
                                              business_name="St. Pius X Academy",
                                              description="This is a primary school established in 2015",
                                              location="Meru County",
                                              category="School")),
                         content_type="application/json")
        self.client.post("/v1/api/businesses",
                         data=json.dumps(dict(owner="tonymputhia@email.com",
                                              business_name="St. Pius XV Academy",
                                              description="This is a secondary school established in 1989",
                                              location="Nakuru County",
                                              category="School")),
                         content_type="application/json")
        response = self.client.get("/v1/api/businesses", content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_view_businesses_by_id(self):
        self.client.post("/api/v1/auth/register",
                         data=json.dumps(dict(username="tony", email="tonymputhia@email.com",
                                              password="Password1*", confirm_password="Password1*")),
                         content_type="application/json")
        self.client.post("/api/v1/auth/login",
                         data=json.dumps(dict(email="tonymputhia@email.com",
                                              password="Password1*")),
                         content_type="application/json")
        self.client.post("/v1/api/businesses",
                         data=json.dumps(dict(owner="tonymputhia@email.com",
                                              business_name="St. Pius X Academy",
                                              description="This is a primary school established in 2015",
                                              location="Meru County",
                                              category="School")),
                         content_type="application/json")
        response = self.client.get("/v1/api/businesses/1",
                                   data=json.dumps(dict(businessId=1)), content_type="application/json")

        self.assertEqual(response.status_code, 200)

    def test_add_review(self):
        self.client.post("/api/v1/auth/register",
                         data=json.dumps(dict(username="tony", email="tonymputhia@email.com",
                                              password="Password1*", confirm_password="Password1*")),
                         content_type="application/json")
        self.client.post("/api/v1/auth/login",
                         data=json.dumps(dict(email="tonymputhia@email.com",
                                              password="Password1*")),
                         content_type="application/json")
        self.client.post("/v1/api/businesses",
                         data=json.dumps(dict(owner="tonymputhia@email.com",
                                              business_name="St. Pius X Academy",
                                              description="This is a primary school established in 2015",
                                              location="Meru County",
                                              category="School")),
                         content_type="application/json")
        response = self.client.post("/v1/api/businesses/1/reviews",
                                    data=json.dumps(dict(owner="tonymputhia@email.com", businessId=1,
                                                         review_name="First Review",
                                                         body="It's a nice clinic")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def get_all_reviews(self):
        self.client.post("/api/v1/auth/register",
                         data=json.dumps(dict(username="tony", email="tonymputhia@email.com",
                                              password="Password1*", confirm_password="Password1*")),
                         content_type="application/json")
        self.client.post("/api/v1/auth/login",
                         data=json.dumps(dict(email="tonymputhia@email.com",
                                              password="Password1*")),
                         content_type="application/json")
        self.client.post("/v1/api/businesses",
                         data=json.dumps(dict(owner="tonymputhia@email.com",
                                              business_name="St. Pius X Academy",
                                              description="This is a primary school established in 2015",
                                              location="Meru County",
                                              category="School")),
                         content_type="application/json")
        response = self.client.post("/v1/api/businesses/1/reviews",
                                   data=json.dumps(dict(owner="tonymputhia@email.com", businessId=1)),
                                   content_type="application/json")

        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        del self.client
