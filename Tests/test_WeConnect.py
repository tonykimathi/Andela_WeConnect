import unittest
from app.models import User


class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def tearDown(self):
        del self.user

    def test_user_created_successfully(self):
        response = self.user.create_user("Tom80", "tom80@email", "password80", "password80")
        self.assertTrue(response, 'User created successfully.')

    def test_signup_with_existing_email(self):
        response = self.user.create_user("Tom808", "tom80@email", "password808", "password808")
        self.assertTrue(response, 'Account with Username already exists. Please log in.')

    def test_signup_with_existing_username(self):
        response = self.user.create_user("Tom80", "tom808@email", "password808", "password808")
        self.assertTrue(response, 'Account with Email already exists. Please log in.')

    def test_length_of_password(self):
        response = self.user.create_user("Tom808", "tom808@email", "pass", "pass")
        self.assertTrue(response, 'Input a password that is at least 6 characters long.')

    def test_passwords_do_not_match(self):
        response = self.user.create_user("Tom808", "tom808@email", "password808", "password80")
        self.assertTrue(response, 'Passwords do not match. Try again.')