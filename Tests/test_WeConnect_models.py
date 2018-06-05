import unittest
from app.user import User
from app.business import Business
from app.reviews import Reviews


class ModelsTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User()
        self.business = Business()
        self.review = Reviews()

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
        self.user.create_user("Tony1", "tony1@email.com", "Password80*", "Password80*")
        response = self.user.login_user("tony1@email.com", "Password80*")
        self.assertEqual(response['msg'], 'Successfully logged in!')

    def test_business_created_successfully(self):
        response = self.business.create_business("tonymputhia@email.com", "Baller Entertainment", "Record Label",
                                                 "Nairobi", "Music")
        self.assertEqual(response['message'], 'Business created successfully.')

    def test_review_created_successfully(self):
        self.business.create_business("tonymputhia@email.com", "Most Entertainment", "Record Label",
                                      "Nairobi", "Music")
        response = self.review.create_review("tonymputhia@email.com", 1, "First Review", "It's a nice clinic")
        self.assertEqual(response['msg'], 'Review added successfully.')

    def test_get_all_reviews_by_business(self):
        response = self.review.get_all_reviews_by_business(1)
        self.assertEqual(response['msg'], 'These are your reviews.')

    def test_business_name_exists(self):
        response = self.business.create_business("tonymputhia@email.com", "Baller Entertainment", "Record Label",
                                                 "Nairobi", "Music")
        self.assertEqual(response['message'], 'Business name already exists. Enter a new one.')

    def test_delete_business(self):
        self.business.create_business("tonymputhia@email.com", "Cooler Entertainment", "Record Label",
                                      "Nairobi", "Music")
        response = self.business.delete_business("tonymputhia@email.com", 2)
        self.assertEqual(response['msg'], 'The business has been deleted successfully.')

    def tearDown(self):
        del self.user
