from app.business import Business


class Reviews(Business):

    def __init__(self):

        """
            Business object initializer.
        """
        super(Business, self).__init__()

        self.reviews_data = []

    def get_all_reviews_by_business(self, business_id):

        """
            Views all reviews about a particular business.
            Arguments:
                Business ID: A unique identifier for the business.
        """

        business_reviews_list = [review for review in self.reviews_data if review['business_id'] == business_id]

        return {"msg": "These are your reviews.", "all_reviews": business_reviews_list}

    def create_review(self, owner, business_id, review_name, body):

        """
            Creates Review objects.
            Arguments:
                owner: A unique identifier for the owner of the review.
                business_id: A unique identifier for the business being reviewed.
                review_name : A unique identify for the Review
                body: Information containing the actual review.
        """
        review_id = len(self.reviews_data) + 1
        review_dict = {}

        for business in Business.business_data:

            if business['business_id'] == business_id:

                review_dict['owner'] = owner
                review_dict['business_id'] = business_id
                review_dict['review_id'] = review_id
                review_dict['review_name'] = review_name
                review_dict['body'] = body

                self.reviews_data.append(review_dict)

                return {"msg": "Review added successfully.", "review_data": review_dict}
            return {"msg": "That business does not exist."}
