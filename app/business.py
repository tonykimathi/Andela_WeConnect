class Business(object):

    business_data = []

    def __init__(self):

        """
            Business object initializer.
        """

    def get_all_businesses(self):

        """
            Views all Business objects.
            Arguments:
                None.
        """

        return {"all_businesses": Business.business_data}

    def get_business_by_id(self, businessId):

        """
            Views a single Business object.
            Arguments:
                Business ID: A unique identifier for the business.
        """

        for business in Business.business_data:
            if businessId == business['businessId']:
                return {"specific_business": business}

    def get_business_by_owner(self, owner):

        """
            Returns businesses belonging to a user
        """
        owner_business_list = [business for business in Business.business_data if business['owner'] == owner]

        return owner_business_list

    def create_business(self, owner, business_name, description, location, category):

        """
            Creates Business objects.
            Arguments:
                User ID: A unique identifier for the user creating the business.
                Business Name: A unique identify for the Business
                Description: Contains descriptive information about the business.
                Location: Shows where business is situated.
                Category: Shows the business type that the business falls under.
        """
        businessId = len(Business.business_data) + 1
        business_dict = {}

        for business in Business.business_data:
            if business['business_name'] == business_name:
                return {"message": "Business name already exists. Enter a new one."}

        business_dict['owner'] = owner
        business_dict['businessId'] = businessId
        business_dict['business_name'] = business_name
        business_dict['description'] = description
        business_dict['location '] = location
        business_dict['category '] = category

        Business.business_data.append(business_dict)

        return {"message": "Business created successfully.", "business_data": business_dict}

    def update_business(self, owner, businessId, business_name, description, location, category):

        """
            Updates Business objects.
            Arguments:
                Business ID: A unique identifier for the business to be updated.
                Business Name: A unique identify for the Business
                Description: Contains descriptive information about the business.
                Location: Shows where business is situated.
                Category: Shows the business type that the business falls under.
        """
        found_business = self.get_business_by_id(businessId)

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

    def delete_business(self, owner, businessId):

        """
            Deletes Business objects.
            Arguments:
                Business ID: A unique identifier for the business to be updated.
        """
        found_business = self.get_business_by_id(businessId)

        if found_business:

            if owner == found_business["specific_business"]['owner']:
                del found_business["specific_business"]

                return {"msg": "The business has been deleted successfully."}
            return {"msg": "You cannot delete a business you do not own."}
        return {"msg": "No such business exists."}

