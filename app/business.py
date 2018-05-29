class Business(object):

    business_data = []

    def __init__(self):

        """
            Business object initializer.
        """

    @staticmethod
    def get_all_businesses():

        """
            Views all Business objects.
            Arguments:
                None.
        """

        return {"all_businesses": Business.business_data}

    @staticmethod
    def get_business_by_id(business_id):

        """
            Views a single Business object.
            Arguments:
                Business ID: A unique identifier for the business.
        """

        for business in Business.business_data:
            if business_id == business['business_id']:
                return {"specific_business": business}

    @staticmethod
    def get_business_by_owner(owner):

        """
            Returns businesses belonging to a user
        """
        owner_business_list = [business for business in Business.business_data if business['owner'] == owner]

        return owner_business_list

    def create_business(self, owner, business_name, description, location, category):

        """
            Creates Business objects.
            Arguments:
                owner: A unique identifier for the user creating the business.
                business_name: A unique identify for the Business
                description: Contains descriptive information about the business.
                location: Shows where business is situated.
                category: Shows the business type that the business falls under.
        """
        business_id = len(Business.business_data) + 1
        business_dict = {}

        if business_name is None:
            return {"msg": "Please input a business name"}
        if description is None:
            return {"msg": "Please input a description."}
        if location is None:
            return {"msg": "Please input a location."}
        if category is None:
            return {"msg": "Please confirm category."}

        for business in Business.business_data:
            if business.get('business_name') == business_name:
                return {"message": "Business name already exists. Enter a new one."}

        business_dict['owner'] = owner
        business_dict['business_id'] = business_id
        business_dict['business_name'] = business_name
        business_dict['description'] = description
        business_dict['location '] = location
        business_dict['category '] = category

        Business.business_data.append(business_dict)

        return {"message": "Business created successfully.", "business_data": business_dict}

    def update_business(self, owner, business_id, business_name, description, location, category):

        """
            Updates Business objects.
            Arguments:
                owner: A unique identifier for the user updating the business.
                business_id : A unique identifier for the business to be updated.
                business_name : A unique identify for the Business
                description: Contains descriptive information about the business.
                location: Shows where business is situated.
                category: Shows the business type that the business falls under.
        """
        found_business = self.get_business_by_id(business_id)

        if found_business:

            if owner == found_business["specific_business"]['owner']:
                found_business["specific_business"]['owner'] = owner
                found_business["specific_business"]['business_name'] = business_name
                found_business["specific_business"]['description'] = description
                found_business["specific_business"]['location '] = location
                found_business["specific_business"]['category '] = category

                Business.business_data.append(found_business)

                return {"msg": "Business updated successfully.", "business_data": found_business}
            return {"msg": "You cannot update a business you do not own."}
        return {"msg": "No such business exists."}

    def delete_business(self, owner, business_id):

        """
            Deletes Business objects.
            Arguments:
                owner: A unique identifier for the user updating the business.
                business_id : A unique identifier for the business to be updated.
        """
        found_business = self.get_business_by_id(business_id)

        if found_business:

            if owner == found_business["specific_business"]['owner']:
                self.business_data[:] = [d for d in self.business_data
                                         if d['business_id'] != found_business["specific_business"]['business_id']]

                return {"msg": "The business has been deleted successfully."}
            return {"msg": "You cannot delete a business you do not own."}
        return {"msg": "No such business exists."}
