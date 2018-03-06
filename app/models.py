class Data():
    """Class containing all user, businesses and reviews data"""

    user_data = [
        {'id': '1',
         'username': 'Tony93',
         'email': 'tonymputhia@emaill.com',
         'password': 'password1',
         },

        {'id': '2',
         'username': 'Tim90',
         'email': 'timmputhia@email.com',
         'password': 'password2'
         }
    ]

    business_data = [
        {'id': '4',
         'name': 'St. Pius X Academy',
         'description': 'This is a primary school that was established in 2015',
         'location': 'Meru County',
         'category': 'School'
         },

        {'id': '5',
         'name': 'Saika Medical Center',
         'description': 'This is a medical clinic that primarily cares for outpatients',
         'location': 'Nairobi County',
         'category': 'Hospital'
         }
    ]

    reviews_data = [
        {'id': '4',
         'title': 'School review',
         'body': 'Really good school with a commendable K.C.P.E record.',
         },

        {'id': '5',
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
                return "Account with Username already exists. Please log in."
            if username == user['username']:
                return "Account with Email already exists. Please log in."

        if len(password) < 6:
            return "Input a password that is at least 6 characters long."

        elif password == confirm_password:
            self.user_dict['username'] = username
            self.user_dict['email'] = email
            self.user_dict['password'] = password

            Data.user_data.append(self.user_dict)

            return "User created successfully."

        return "Passwords do not match. Try again."



