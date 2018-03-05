class Data():
    """Class containing all user, businesses and reviews data"""
    def __init__(self):

        self.user_data = [
            {'id': '1',
             'first_name': 'Tony',
             'last_name': 'Mputhia',
             'email': 'tonymputhia@emaill.com',
             'password': 'password1'},

            {'id': '2',
             'first_name': 'Tim',
             'last_name': 'Mputhia',
             'email': 'timmputhia@email.com',
             'password': 'password2'}
        ]

        self.business_data = [
            {
                'id': '4',
                'name': 'St. Pius X Academy',
                'description': 'This is a primary school that was established in 2015',
                'location': 'Meru County',
                'category': 'School'
            },
            {
                'id': '5',
                'name': 'Saika Medical Center',
                'description': 'This is a medical clinic that primarily cares for outpatients',
                'location': 'Nairobi County',
                'category': 'Hospital'
            }
        ]

        self.reviews_data = [
            {
                'id': '4',
                'name': 'St. Pius X Academy',
                'description': 'This is a primary school that was established in 2015',
                'location': 'Meru County',
                'category': 'School'
            },
            {
                'id': '5',
                'name': 'Saika Medical Center',
                'description': 'This is a medical clinic that primarily cares for outpatients',
                'location': 'Nairobi County',
                'category': 'Hospital'
            }
        ]

