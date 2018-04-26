from app.data import Data


class Reviews():

    def __init__(self):

        """
            Business object initializer.
        """

        self.review_dict = {}

    def create_review(self, owner, businessId, review_name, body):

        """
            Creates Review objects.
            Arguments:
                Business ID: A unique identifier for the business being reviewed.
                Review Name: A unique identify for the Review
                Body: Information containing the actual review.
        """
        review_id = len(Data.reviews_data) + 1

        for review in Data.reviews_data:
            if businessId == review['businessId']:

                self.review_dict['owner'] = owner
                self.review_dict['businessId'] = businessId
                self.review_dict['review_id'] = review_id
                self.review_dict['review_name'] = review_name
                self.review_dict['body'] = body

                Data.reviews_data.append(self.review_dict)

                return {"msg": "Review added successfully.", "review_data": self.review_dict}, 201
            return {"msg": "That business does not exist."}

    @staticmethod
    def get_all_reviews(businessId):

        """
            Views all reviews about a particular business.
            Arguments:
                Business ID: A unique identifier for the business.
        """

        for review in Data.reviews_data:
            if businessId == review['businessId']:
                return {"all_reviews": Data.reviews_data}