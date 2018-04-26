class Data():
    """Class containing all user, businesses and reviews data"""

    user_data = [
        {'user_id': 1,
         'username': 'Tony93',
         'email': 'tonymputhia@email.com',
         'password': 'Password1*',
         },

        {'user_id': 2,
         'username': 'Tim90',
         'email': 'timmputhia@email.com',
         'password': 'Password2*'
         }
    ]

    business_data = [
        {'businessId': 1,
         'owner': 'tonymputhia@email.com',
         'business_name': 'St. Pius X Academy',
         'description': 'This is a primary school that was established in 2015',
         'location': 'Meru County',
         'category': 'School'
         },

        {'businessId': 2,
         'owner': 'timmputhia@email.com',
         'business_name': 'Saika Medical Center',
         'description': 'This is a medical clinic that primarily cares for outpatients',
         'location': 'Nairobi County',
         'category': 'Hospital'
         }
    ]

    reviews_data = [
        {'review_id': 1,
         'owner': 'tonymputhia@email.com',
         'businessId': '1',
         'review_name': 'School review',
         'body': 'Really good school with a commendable K.C.P.E record.',
         },

        {'review_id': 2,
         'owner': 'timmputhia@email.com',
         'businessId': '2',
         'review_name': 'Hospital review',
         'body': 'I did not like the customer service',
         }
    ]
