from app.data import Data


class Business():

    def __init__(self):

        """
            Business object initializer.
        """

        self.business_dict = {}

    @classmethod
    def get_all_businesses(cls):

        """
            Views all Business objects.
            Arguments:
                None.
        """

        return {"all_businesses": Data.business_data}

    @classmethod
    def get_business_by_id(cls, businessId):

        """
            Views a single Business object.
            Arguments:
                Business ID: A unique identifier for the business.
        """

        for business in Data.business_data:
            if businessId == business['businessId']:
                return {"specific_business": business}

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
        businessId = len(Data.business_data) + 1

        for business in Data.business_data:
            if business_name == business['business_name']:
                return {"msg": "Business name already exists. Enter a new one."}

            self.business_dict['owner'] = owner
            self.business_dict['businessId'] = businessId
            self.business_dict['business_name'] = business_name
            self.business_dict['description'] = description
            self.business_dict['location '] = location
            self.business_dict['category '] = category

            Data.business_data.append(self.business_dict)

            return {"msg": "Business created successfully.", "business_data": self.business_dict}

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
        found_business = Business.get_business_by_id(businessId)
        found_businessId = found_business['specific_business']['businessId']

        if found_businessId == businessId:
            found_business['specific_business']['owner'] = owner
            found_business['specific_business']['business_name'] = business_name
            found_business['specific_business']['description'] = description
            found_business['specific_business']['location '] = location
            found_business['specific_business']['category '] = category

            Data.business_data.append(self.business_dict)

            return {"msg": "Business updated successfully.", "business_data": self.business_dict}
        return {"msg": "The Business does not exist."}

    @staticmethod
    def delete_business(owner, businessId):

        """
            Deletes Business objects.
            Arguments:
                Business ID: A unique identifier for the business to be updated.
        """

        for business in Data.business_data:
            if owner == business["owner"]:
                if businessId == business['businessId']:
                    del business

                    return {"msg": "The business has been deleted successfully."}
                return {"msg": "No such business exists."}
            return {"msg": "You cannot delete a business you do not own."}

