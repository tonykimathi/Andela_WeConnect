from app.business import Business


class Reviews(Business):

    def __init__(self):

        """
            Business object initializer.
        """
        super().__init__()

        self.reviews_data = []

    def get_all_reviews_by_business(self, businessId):

        """
            Views all reviews about a particular business.
            Arguments:
                Business ID: A unique identifier for the business.
        """

        business_reviews_list = [review for review in self.reviews_data if review['businessId'] == businessId]

        return {"all_reviews": business_reviews_list}

    def create_review(self, owner, businessId, review_name, body):

        """
            Creates Review objects.
            Arguments:
                Business ID: A unique identifier for the business being reviewed.
                Review Name: A unique identify for the Review
                Body: Information containing the actual review.
        """
        review_id = len(self.reviews_data) + 1
        review_dict = {}

        for business in Business.business_data:

            if business['businessId'] == businessId:

                review_dict['owner'] = owner
                review_dict['businessId'] = businessId
                review_dict['review_id'] = review_id
                review_dict['review_name'] = review_name
                review_dict['body'] = body

                self.reviews_data.append(review_dict)

                return {"msg": "Review added successfully.", "review_data": review_dict}
            return {"msg": "That business does not exist."}
        return {"msg": "unsuccessful."}
