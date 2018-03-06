import unittest
from app.models import User


class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def tearDown(self):
        del self.user

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