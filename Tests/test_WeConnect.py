import unittest
import json
from app.user import User
from app.business import Business
from app.views import app


class ModelsTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User()
        self.business = Business()

    def test_user_created_successfully(self):
        response = self.user.create_user("Tonto", "tonto@email.com", "Password80*", "Password80*")
        self.assertEqual(response['msg'], 'User created successfully.')

    def test_signup_with_existing_email(self):
        self.user.create_user("Tom", "tom@email.com", "Password80*", "Password80*")
        response = self.user.create_user("Tom2", "tom@email.com", "password80", "password80")
        self.assertEqual(response['msg'], 'Account with Email already exists. Please log in.')

    def test_signup_with_wrong_email_format(self):
        response = self.user.create_user("Tom2", "tom@email", "Password80*", "Password80*")
        self.assertEqual(response['msg'], 'Please provide a valid email address')

    def test_signup_with_wrong_username_format(self):
        response = self.user.create_user("Tom2@", "tom@email", "Password80*", "Password80*")
        self.assertEqual(response['msg'], 'These special characters (. , ! space []) should not be in your username.')

    def test_signup_with_existing_username(self):
        self.user.create_user("Tom", "tom808@email.com", "Password808*", "Password808*")
        response = self.user.create_user("Tom", "tom8082@email", "password808", "password808")
        self.assertEqual(response['msg'], 'Account with Username already exists. Please log in.')

    def test_length_of_password(self):
        response = self.user.create_user("Tom808", "tom808@email.com", "pass", "pass")
        self.assertEqual(response['msg'], 'Input a password that is at least 6 characters long.')

    def test_signup_with_wrong_password_format(self):
        response = self.user.create_user("Tom20", "tom20@email.com", "password80", "password80")
        self.assertEqual(response['msg'], 'Your password should have at least 1 capital letter, special character'
                                          ' and number.')

    def test_passwords_do_not_match(self):
        response = self.user.create_user("Tom808", "tom808@email.com", "Password808*", "Password808")
        self.assertEqual(response['msg'], 'Passwords do not match. Try again.')

    def test_failed_login(self):
        response = self.user.login_user("tonto@email.com", "Password80*")
        self.assertEqual(response['msg'], 'You have no account,please sign up')

    def test_successful_login(self):
        response = self.user.login_user("tonymputhia@email.com", "Password1*")
        self.assertEqual(response['msg'], 'Successfully logged in!')

    def test_business_created_successfully(self):
        response = self.business.create_business("1", "Baller Entertainment", "Record Label", "Nairobi", "Music")
        self.assertEqual(response['msg'], 'Business created successfully.')

    def test_business_name_exists(self):
        response = self.business.create_business("2", "St. Pius X Academy", "Record Label", "Nairobi", "Music")
        self.assertEqual(response['msg'], 'Business name already exists. Enter a new one.')

    def tearDown(self):
        del self.user


class EndpointsTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(self)

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

    def test_reset_password(self):
        self.client.post("/api/v1/auth/reset-password",
                         data=json.dumps(dict(email="timmputhia45@email.com",
                                              password="Password234*", confirm_password="Password234*")),
                         content_type="application/json")
        response = self.client.post("/api/v1/auth/reset-password",
                                    data=json.dumps(dict(email="timmputhia45@email.com",
                                                         password="Password2345*", confirm_password="Password2345*")),
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
        response = self.client.post("/v1/api/businesses",
                                    data=json.dumps(dict(user_id="3", business_name="St. Pius X Academy",
                                                         description="This is a primary school established in 2015",
                                                         location="Meru County",
                                                         category="School")),
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
        self.client.post("/v1/api/businesses",
                         data=json.dumps(dict(user_id="3", business_name="St. Pius X Academy",
                                              description="This is a primary school established in 2015",
                                              location="Meru County",
                                              category="School")),
                         content_type="application/json")
        response = self.client.put("/v1/api/businesses/<businessId>",
                                   data=json.dumps(dict(businessId="3", business_name="Gilgil Academy",
                                                        description="This is a secondary school established in 2015",
                                                        location="Lodwar County",
                                                        category="School")),
                                   content_type="application/json")
        self.assertEqual(response.status_code, 204)
