from app.data import Data


class Business():

    def __init__(self):
        self.business_dict = {}
        self.businessId = len(Data.business_data) + 1

    @staticmethod
    def get_all_businesses():
        return {"all_businesses": Data.business_data}

    @staticmethod
    def get_business_by_id(businessId):
        for business in Data.business_data:
            if businessId == business['businessId']:
                return {"specific_businesses": business}

    def create_business(self, user_id, business_name, description, location, category):

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
        for business in Data.business_data:
            if businessId == business['businessId']:
                del business
                return {"msg": "The business has been deleted successfully."}

