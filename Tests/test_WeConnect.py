import unittest
import json
from app.models import User
# from app import create_app
from app.views import app


class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_user_created_successfully(self):
        response = self.user.create_user("Tonto", "tonto@email", "password80", "password80")
        self.assertEqual(response, 'User created successfully.')

    def test_signup_with_existing_email(self):
        self.user.create_user("Tom", "tom@email", "password80", "password80")
        response = self.user.create_user("Tom2", "tom@email", "password80", "password80")
        self.assertEqual(response, 'Account with Email already exists. Please log in.')

    def test_signup_with_existing_username(self):
        self.user.create_user("Tom", "tom808@email", "password808", "password808")
        response = self.user.create_user("Tom", "tom8082@email", "password808", "password808")
        self.assertEqual(response, 'Account with Username already exists. Please log in.')

    def test_length_of_password(self):
        response = self.user.create_user("Tom808", "tom808@email", "pass", "pass")
        self.assertEqual(response, 'Input a password that is at least 6 characters long.')

    def test_passwords_do_not_match(self):
        response = self.user.create_user("Tom808", "tom808@email", "password808", "password80")
        self.assertEqual(response, 'Passwords do not match. Try again.')

    def test_failed_login(self):
        response = self.user.login_user("tonto@email", "password80")
        self.assertEqual(response, 'You have no account,please sign up')

    def test_successful_login(self):
        response = self.user.login_user("tonymputhia@email.com", "password1")
        self.assertEqual(response, 'Successfully logged in!')

    def tearDown(self):
        del self.user


class UserEndpointsTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(self)
        self.client.post("/api/v1/auth/register",
                         data=json.dumps(dict(username="tony", email="tonymputhia@email.com",
                                              password="password1", confirm_password="password1")),
                         content_type="application/json")

    def test_successful_registration(self):
        response = self.client.post("/api/v1/auth/register",
                                    data=json.dumps(dict(username="tim", email="timmputhia@email.com",
                                                         password="password234", confirm_password="password234")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_already_registered(self):
        response = self.client.post("/api/v1/auth/register",
                                    data=json.dumps(dict(username="tony", email="tonymputhia@email.com",
                                                         password="password1", confirm_password="password1")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 404)


