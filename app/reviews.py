from app.data import Data


class Reviews():
    review_id = len(Data.reviews_data) + 1

    def __init__(self):
        self.review_dict = {}
        self.review_id = len(Data.reviews_data) + 1

    def create_review(self, businessId, review_name, body):
        for review in Data.reviews_data:
            if businessId == review['businessId']:
                self.review_dict['businessId'] = self.review_id
                self.review_dict['review_name'] = review_name
                self.review_dict['body'] = body

                Data.reviews_data.append(self.review_dict)

                return {"msg": "Review added successfully.", "review_data": self.review_dict}
            return {"msg": "That business does not exist."}

    @staticmethod
    def get_all_reviews(businessId):
        for review in Data.reviews_data:
            if businessId == review['businessId']:
                return {"all_reviews": Data.reviews_data}