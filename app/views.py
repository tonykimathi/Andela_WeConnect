from flask_api import FlaskAPI
from flask import jsonify, request, session
from app.user import User
from app.business import Business
from app.reviews import Reviews


user_object = User()
business_object = Business()
review_object = Reviews()

app = FlaskAPI(__name__, instance_relative_config=True)
app.secret_key = 'youwouldneverguessthis'
app.config.from_object('config')
app.config.from_pyfile('config.py')


@app.route('/')
def home_route():
    """ Home route """
    response = jsonify({'greetings': 'Greetings and welcome to weConnect API'})
    return response, 200


@app.route('/api/v1/auth/register', methods=['POST'])
def signup():
    if request.method == "POST":
        username = request.json['username']
        email = request.json['email']
        password = request.json['password']
        confirm_password = request.json['confirm_password']
        msg = user_object.create_user(username, email, password, confirm_password)

        if msg['msg'] == 'User created successfully.':
            return jsonify(msg), 201
        elif msg['msg'] == 'Account with Username already exists. Please log in.' or \
                'Account with Email already exists. Please log in.' or 'Passwords do not match. Try again.':
            return jsonify(msg), 403


@app.route('/api/v1/auth/login', methods=['GET', 'POST'])
def login():
    """ User login """
    if request.method == "POST":
        password = request.json['password']
        session['email'] = request.json['email']
        msg = user_object.login_user(session['email'], password)

        if msg['msg'] == 'Successfully logged in!':
            return jsonify(msg), 200
        elif msg['msg'] == 'Wrong Password. Try again.' or 'You have no account,please sign up':
            return jsonify(msg), 401


@app.route('/api/v1/auth/logout', methods=['POST'])
def logout():
    """ User logout """
    if request.method == "POST":
        if 'email' in session:
            session.pop('email', None)
            return jsonify({"message": "Logout successful"}), 200


@app.route('/api/v1/auth/reset-password', methods=['POST'])
def reset_password():
    """ User reset password """
    if request.method == "POST":
        email = request.json['email']
        new_password = request.json['new_password']
        confirm_new_password = request.json['confirm_new_password']

        msg = user_object.reset_password(email, new_password, confirm_new_password)

        return jsonify(msg), 200


@app.route('/v1/api/businesses', methods=['POST'])
def create_business():
    if 'email' in session:
        if request.method == "POST":
            owner = session['email']
            business_name = request.json['business_name']
            description = request.json['description']
            location = request.json['location']
            category = request.json['category']

            msg = business_object.create_business(owner, business_name, description, location, category)

            if msg["message"] == "Business created successfully.":
                return jsonify(msg), 201
            return jsonify(msg), 403


@app.route('/v1/api/businesses/<int:businessId>', methods=['PUT'])
def update_business_profile(businessId):
    if session.get('email') is not None:
        if request.method == "PUT":

            owner = session['email']
            business_name = request.json['business_name']
            description = request.json['description']
            location = request.json['location']
            category = request.json['category']

            msg = business_object.update_business(owner, businessId, business_name, description, location, category)
            if msg['msg'] == 'Business updated successfully.':
                return jsonify(msg), 200
            return jsonify(msg), 403


@app.route('/v1/api/businesses/<int:businessId>', methods=['DELETE'])
def delete_business(businessId):
    if session.get('email') is not None:
        if request.method == "DELETE":
            owner = session['email']
            msg = business_object.delete_business(owner, businessId)
            return jsonify(msg), 200


@app.route('/v1/api/businesses', methods=['GET'])
def get_businesses():
    if session.get('email') is not None:
        if request.method == "GET":
            msg = business_object.get_all_businesses()
            return jsonify(msg), 200


@app.route('/v1/api/businesses/<int:businessId>', methods=['GET'])
def get_business_by_id(businessId):
    if session.get('email') is not None:
        if request.method == "GET":
            msg = business_object.get_business_by_id(businessId)
            return jsonify(msg), 200


@app.route('/v1/api/businesses/<int:businessId>/reviews', methods=['POST'])
def add_review(businessId):
    if session.get('email') is not None:
        if request.method == "POST":
            owner = session['email']
            review_name = request.json['review_name']
            body = request.json['body']
            msg = review_object.create_review(owner, businessId, review_name, body)
            return jsonify(msg), 201


@app.route('/v1/api/businesses/<int:businessId>/reviews', methods=['GET'])
def get_all_reviews(businessId):
    if session.get('email') is not None:
        if request.method == "GET":
            msg = review_object.get_all_reviews_by_business(businessId)
            return jsonify(msg), 200
