from flask_api import FlaskAPI
from flask import jsonify, request, session
from app.models import User


user_object = User()

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
        response = jsonify(msg)
        # response.status_code = 201
        return response


@app.route('/api/v1/auth/login', methods=['GET', 'POST'])
def login():
    """ User login """
    if request.method == "POST":
        email = request.json['email']
        password = request.json['password']
        session['email'] = email
        msg = user_object.login_user(email, password)
        response = jsonify(msg)
        # response.status_code = 200
        return response


@app.route('/api/v1/auth/logout', methods=['POST'])
def logout():
    """ User logout """
    if session.get('email') is not None:
        session.pop('email', None)
        return jsonify({"message": "Logout successful"})
    return jsonify({"message": "You are not logged in"})


