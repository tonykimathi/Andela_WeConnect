from flask import jsonify, request
from app.models import User
from run import app

user_object = User()


# Home route
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
        cpassword = request.json['cpassword']
        msg = user_object.create_user(username, email, password, cpassword)
        response = jsonify(msg)
        response.status_code = 201
        return response
