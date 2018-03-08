import re


class Data():
    """Class containing all user, businesses and reviews data"""

    user_data = [
        {'id': '1',
         'username': 'Tony93',
         'email': 'tonymputhia@email.com',
         'password': 'Password1*',
         },

        {'id': '2',
         'username': 'Tim90',
         'email': 'timmputhia@email.com',
         'password': 'Password2*'
         }
    ]

    business_data = [
        {'business_id': '4',
         'business_name': 'St. Pius X Academy',
         'description': 'This is a primary school that was established in 2015',
         'location': 'Meru County',
         'category': 'School'
         },

        {'business_id': '5',
         'business_name': 'Saika Medical Center',
         'description': 'This is a medical clinic that primarily cares for outpatients',
         'location': 'Nairobi County',
         'category': 'Hospital'
         }
    ]

    reviews_data = [
        {'review_id': '4',
         'title': 'School review',
         'body': 'Really good school with a commendable K.C.P.E record.',
         },

        {'review_id': '5',
         'title': 'Hospital review',
         'body': 'I did not like the customer service',
         }
    ]


class User():
    def __init__(self):
        self.user_dict = {}
        self.id = len(Data.user_data) + 1

    def create_user(self, username, email, password, confirm_password):

        for user in Data.user_data:
            if email == user['email']:
                return "Account with Email already exists. Please log in."
            elif username == user['username']:
                return "Account with Username already exists. Please log in."
        if len(password) < 6:
            return "Input a password that is at least 6 characters long."

        elif not re.match("^[a-zA-Z0-9_]*$", username):
            return "These special characters (. , ! space []) should not be in your username."

        elif not re.match(r"(^[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-z]+$)", email):
            return "Please provide a valid email address"

        elif re.match("^[a-zA-Z0-9_]*$", password):
            return "Your password should have at least 1 capital letter, special character and number."

        if password == confirm_password:
            self.user_dict['id'] = self.id
            self.user_dict['username'] = username
            self.user_dict['email'] = email
            self.user_dict['password'] = password

            Data.user_data.append(self.user_dict)
        else:
            return "Passwords do not match. Try again."
        return "User created successfully."

    @staticmethod
    def login_user(email, password):
        for user in Data.user_data:
            if email == user['email']:
                if password == user['password']:
                    return "Successfully logged in!"
                return "Wrong Password. Try again."
        return "You have no account,please sign up"

    def reset_password(self, email, new_password, confirm_new_password):
        for user in Data.user_data:
            if email == user['email']:
                if new_password == confirm_new_password:
                    self.user_dict['password'] = new_password
                    return "Your password has been reset"



