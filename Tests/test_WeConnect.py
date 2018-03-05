import unittest
from app.models import User


class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User("1", "Tony", "Mputhia", "tonymputhia@email", "password1")

    def tearDown(self):
        del self.user

    def test_user_created_successfully(self):
        self.assertTrue(self.user.create_user(), 'User created successfully')