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

        if msg == 'User created successfully.':
            return jsonify(msg), 201
        elif msg == 'Account with Username already exists. Please log in.' or \
                'Account with Email already exists. Please log in.' or 'Passwords do not match. Try again.':
            return jsonify(msg), 403


@app.route('/api/v1/auth/login', methods=['GET', 'POST'])
def login():
    """ User login """
    if request.method == "POST":
        email = request.json['email']
        password = request.json['password']
        session['email'] = email
        msg = user_object.login_user(email, password)
        response = jsonify(msg)
        return response


@app.route('/api/v1/auth/logout', methods=['POST'])
def logout():
    """ User logout """
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




