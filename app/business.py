from app.data import Data


class Business():

    def __init__(self):

        """
            Business object initializer.
        """

        self.business_dict = {}
        self.businessId = len(Data.business_data) + 1

    @staticmethod
    def get_all_businesses():

        """
            Views all Business objects.
            Arguments:
                None.
        """

        for business in Data.business_data:
            return {"all_businesses": business}

    @staticmethod
    def get_business_by_id(businessId):

        """
            Views a single Business object.
            Arguments:
                Business ID: A unique identifier for the business.
        """

        for business in Data.business_data:
            if businessId == business['businessId']:
                return {"specific_businesses": business}

    def create_business(self, user_id, business_name, description, location, category):

        """
            Creates Business objects.
            Arguments:
                User ID: A unique identifier for the user creating the business.
                Business Name: A unique identify for the Business
                Description: Contains descriptive information about the business.
                Location: Shows where business is situated.
                Category: Shows the business type that the business falls under.
        """

        for business in Data.business_data:
            if business_name == business['business_name']:
                return {"msg": "Business name already exists. Enter a new one."}
            for user in Data.user_data:
                if user_id == user['user_id']:
                    self.business_dict['user_id'] = user_id
                    self.business_dict['businessId'] = self.businessId
                    self.business_dict['business_name'] = business_name
                    self.business_dict['description'] = description
                    self.business_dict['location '] = location
                    self.business_dict['category '] = category

                    Data.business_data.append(self.business_dict)

                    return {"msg": "Business created successfully.", "business_data": self.business_dict}

                return {"msg": "No such user exists."}

    def update_business(self, businessId, business_name, description, location, category):

        """
            Updates Business objects.
            Arguments:
                Business ID: A unique identifier for the business to be updated.
                Business Name: A unique identify for the Business
                Description: Contains descriptive information about the business.
                Location: Shows where business is situated.
                Category: Shows the business type that the business falls under.
        """

        for business in Data.business_data:
            if businessId == business['businessId']:
                self.business_dict['businessId'] = businessId
                self.business_dict['business_name'] = business_name
                self.business_dict['description'] = description
                self.business_dict['location '] = location
                self.business_dict['category '] = category

                Data.business_data.append(self.business_dict)

                return {"msg": "Business updated successfully.", "business_data": self.business_dict}
            return {"msg": "The Business does not exist."}

    @staticmethod
    def delete_business(businessId):

        """
            Deletes Business objects.
            Arguments:
                Business ID: A unique identifier for the business to be updated.
        """

        for business in Data.business_data:
            if businessId == business['businessId']:
                del business
                return {"msg": "The business has been deleted successfully."}

