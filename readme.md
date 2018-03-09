[![Build Status](https://travis-ci.org/tonykimathi/Andela_WeConnect.svg?branch=ft-user-registration-login-155701739)](https://travis-ci.org/tonykimathi/Andela_WeConnect)
[![Coverage Status](https://coveralls.io/repos/github/tonykimathi/Andela_WeConnect/badge.svg?branch=Develop)](https://coveralls.io/github/tonykimathi/Andela_WeConnect?branch=Develop)
# WeConnect

WeConnect provides a platform that brings businesses and individuals together. 
This platform creates awareness for businesses and gives the users the ability 
to write reviews about the businesses they have interacted with.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

##### Clone this repository

> https://github.com/tonykimathi/Andela_WeConnect.git

1. ##### Create a virtual environment

   ​	Use this [**guide**](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/).

   ​	Activate the  virtual environment.

2. ##### Install project dependencies

     run the command `pip -r install requirements.txt` on the command line
     
### Usage

To test our project on your terminal run 

``` export FLASK_APP=run.py```

then

``` flask run ```

on your browser open up [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

### Api Endpoints

| Endpoint | Functionality |
| -------- | ------------- |
| POST /api/v1/auth/register | Creates a user account |
| POST /api/v1/auth/login | Logs in a user |
| POST /api/v1/auth/logout | Logs out a user |
| POST /api/v1/auth/reset-password  | Password reset |
| POST /v1/api/businesses | Register a business |
| GET /v1/api/businesses  | Retrieves all businesses |
| PUT /v1/api/businesses/<businessId> | Updates a business profile |
| DELETE /v1/api/businesses/<businessId> | Remove a business |
| GET /v1/api/businesses | Get businesses |
| GET /v1/api/businesses/<businessId> | Get one business |
| POST /v1/api/businesses/<businessId>/reviews | Add a review for a business |
| GET /v1/api/businesses/<businessId>/reviews | Get all reviews for a business |

## Author

* [tonykimathi](https://github.com/tonykimathi)
