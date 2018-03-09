from flask_api import FlaskAPI
from flask import jsonify, request, session
from app.user import User
from app.business import Business
from app.reviews import Reviews


user_object = User()
business_object = Business()
review_object = Reviews()

app = FlaskAPI(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')


@app.route('/')
def home_route():
    """ Home route """
    response = jsonify({'greetings': 'Greetings and welcome to weConnect API'})
    return response


@app.route('/api/v1/auth/register', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        username = request.json['username']
        email = request.json['email']
        password = request.json['password']
        confirm_password = request.json['confirm_password']
        msg = user_object.create_user(username, email, password, confirm_password)

        if msg['msg'] == 'User created successfully.':
            return jsonify(msg['msg']), 201
        elif msg['msg'] == 'Account with Username already exists. Please log in.' or \
                'Account with Email already exists. Please log in.' or 'Passwords do not match. Try again.':
            return jsonify(msg['msg']), 403
    return jsonify({"message": "Incorrect http verb"})


@app.route('/api/v1/auth/login', methods=['GET', 'POST'])
def login():
    """ User login """
    if request.method == "POST":
        email = request.json['email']
        password = request.json['password']
        session['email'] = email
        msg = user_object.login_user(email, password)
        response = jsonify(msg['msg'])
        return response
    return jsonify({"message": "Incorrect http verb"})


@app.route('/api/v1/auth/logout', methods=['POST'])
def logout():
    """ User logout """
    if request.method == "POST":
        if session.get('email') is not None:
            session.pop('email', None)
            return jsonify({"message": "Logout successful"})
    return jsonify({"message": "You are not logged in"})


@app.route('/api/v1/auth/reset-password', methods=['POST'])
def reset_password():
    """ User reset password """
    if request.method == "POST":
        email = request.json['email']
        password = request.json['password']
        confirm_password = request.json['confirm_password']
        msg = user_object.reset_password(email, password, confirm_password)
        return jsonify(msg), 200
    return jsonify({"message": "Incorrect http verb"})


@app.route('/v1/api/businesses', methods=['GET', 'POST'])
def create_business():
    if request.method == "POST":
        user_id = request.json['user_id']
        business_name = request.json['business_name']
        description = request.json['description']
        location = request.json['location']
        category = request.json['category']
        msg = business_object.create_business(user_id, business_name, description, location, category)
        return jsonify(msg['msg']), 201
    return jsonify({"message": "Incorrect http verb"})


@app.route('/v1/api/businesses/<businessId>', methods=['PUT'])
def update_business_profile(businessId):
    if request.method == "PUT":
        business_name = request.json['business_name']
        description = request.json['description']
        location = request.json['location']
        category = request.json['category']

        msg = business_object.update_business(businessId, business_name, description, location, category)
        return jsonify(msg['msg']), 204
    return jsonify({"message": "Incorrect http verb"})


@app.route('/v1/api/businesses/<businessId>', methods=['DELETE'])
def delete_business(businessId):
    if request.method == "DELETE":
        msg = business_object.delete_business(businessId)
        return jsonify(msg), 204
    return jsonify({"message": "Incorrect http verb"})


@app.route('/v1/api/businesses', methods=['GET'])
def get_businesses():
    if request.method == "GET":
        msg = business_object.get_all_businesses()
        return jsonify(msg), 200
    return jsonify({"message": "Incorrect http verb"})


@app.route('/v1/api/businesses/<businessId>', methods=['GET'])
def get_business_by_id(businessId):
    if request.method == "GET":
        msg = business_object.get_business_by_id(businessId)
        return jsonify(msg)
    return jsonify({"message": "Incorrect http verb"}), 200


@app.route('/v1/api/businesses/<businessId>/reviews', methods=['POST'])
def add_review(businessId):
    if request.method == "POST":
        review_name = request.json['review_name']
        body = request.json['body']
        msg = review_object.create_review(businessId, review_name, body)
        return jsonify(msg['msg']), 201
    return jsonify({"message": "Incorrect http verb"})

@app.route('/v1/api/businesses/<businessId>/reviews', methods=['GET'])
def get_all_reviews(businessId):
    if request.method == "GET":
        msg = review_object.get_all_reviews(businessId)
        return jsonify(msg['msg']), 200
    return jsonify({"message": "Incorrect http verb"})


