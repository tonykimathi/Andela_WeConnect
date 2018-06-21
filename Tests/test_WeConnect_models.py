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

    def test_signup_with_wrong_credentials(self):
        response1 = self.user.create_user("Tom2", None, "Password80*", "Password80*")
        response2 = self.user.create_user(None, "tom@email.com", "Password80*", "Password80*")
        response3 = self.user.create_user("Tom2", "tom@email.com", None, "Password80*")
        response4 = self.user.create_user("Tom2", "tom@email.com", "Password80*", None)
        self.assertEqual(response1['msg'], 'Please input an email address')
        self.assertEqual(response2['msg'], 'Please input a username.')
        self.assertEqual(response3['msg'], 'Please input a password.')
        self.assertEqual(response4['msg'], 'Please confirm password.')

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

    def test_login_with_wrong_credentials(self):
        response1 = self.user.login_user(None, "Password80*")
        response2 = self.user.login_user("tom@email.com", None)
        self.assertEqual(response1['msg'], 'Please input an email address')
        self.assertEqual(response2['msg'], 'Please input a password.')

    def test_reset_password(self):
        self.user.create_user("Tony2", "tony2@email.com", "Password80*", "Password80*")
        self.user.login_user("tony1@email.com", "Password80*")
        response = self.user.reset_password("tony2@email.com", "Password808*", "Password808*")
        self.assertEqual(response['message'], "Your password has been reset")
        response2 = self.user.reset_password("tony2@email.com", "Password808*", "Password80*")
        self.assertEqual(response2['msg'], "Passwords don't match")

    def test_failed_reset_password(self):
        response = self.user.reset_password("tony2@email.com", "Password808*", "Password808*")
        self.assertEqual(response['msg'], "You have no account, please sign up")

    def test_reset_password_wrong_credentials(self):
        response1 = self.user.reset_password(None, "Password80*", "Password80*")
        response2 = self.user.reset_password("tom@email.com", None, "Password80*")
        response3 = self.user.reset_password("tom@email.com", "Password80*", None)
        self.assertEqual(response1['msg'], 'Please input an email address')
        self.assertEqual(response2['msg'], 'Please input a new password.')
        self.assertEqual(response3['msg'], 'Please confirm your new password.')

    def test_business_created_successfully(self):
        response = self.business.create_business("tonymputhia@email.com", "Baller Entertainment", "Record Label",
                                                 "Nairobi", "Music")
        self.assertEqual(response['message'], 'Business created successfully.')

    def test_create_business_wrong_credentials(self):
        response1 = self.business.create_business("tonymputhia@email.com", None, "Record Label",
                                                  "Nairobi", "Music")
        response2 = self.business.create_business("tonymputhia@email.com", "Baller Entertainment", None,
                                                  "Nairobi", "Music")
        response3 = self.business.create_business("tonymputhia@email.com", "Baller Entertainment", "Record Label",
                                                  None, "Music")
        response4 = self.business.create_business("tonymputhia@email.com", "Baller Entertainment", "Record Label",
                                                  "Meru", None)
        self.assertEqual(response1['msg'], 'Please input a business name')
        self.assertEqual(response2['msg'], 'Please input a description.')
        self.assertEqual(response3['msg'], 'Please input a location.')
        self.assertEqual(response4['msg'], 'Please confirm category.')

    def test_review_created_successfully(self):
        self.business.create_business("tonymputhia@email.com", "Most Entertainment", "Record Label",
                                      "Nairobi", "Music")
        response = self.review.create_review("tonymputhia@email.com", 1, "First Review", "It's a nice clinic")
        self.assertEqual(response['msg'], 'Review added successfully.')

    def test_review_created_unsuccessfully(self):
        response = self.review.create_review("tonymputhia@email.com", 3, "First Review", "It's a nice clinic")
        self.assertEqual(response['msg'], 'That business does not exist.')

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

    def test_failed_delete_business(self):
        self.business.create_business("tonymputhia@email.com", "Y-Not Entertainment", "Record Label",
                                      "Nairobi", "Music")
        response = self.business.delete_business("tonymputhia26@email.com", 2)
        self.assertEqual(response['msg'], 'You cannot delete a business you do not own.')
        response2 = self.business.delete_business("tonymputhia@email.com", 3)
        self.assertEqual(response2['msg'], 'No such business exists.')

    def tearDown(self):
        del self.user
