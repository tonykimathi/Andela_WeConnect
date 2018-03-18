import re
from app.data import Data


class User():

    def __init__(self):

        """
            User object initializer.
        """

        self.user_dict = {}
        self.user_id = len(Data.user_data) + 1

    def create_user(self, username, email, password, confirm_password):

        """
            Creates user objects.
            Arguments:
                Username: A unique identifier for the user.
                Email: Personal email of the user.
                Password: A secret security key.
        """

        if email is None:
            return {"msg": "Please input an email address"}
        if username is None:
            return {"msg": "Please input a username."}
        if password is None:
            return {"msg": "Please input a password."}

        for user in Data.user_data:
            if email == user['email']:
                return {"msg": "Account with Email already exists. Please log in."}
            elif username == user['username']:
                return {"msg": "Account with Username already exists. Please log in."}

        if len(password) < 6:
            return {"msg": "Input a password that is at least 6 characters long."}

        elif not re.match("^[a-zA-Z0-9_]*$", username):
            return {"msg": "These special characters (. , ! space []) should not be in your username."}

        elif not re.match(r"(^[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-z]+$)", email):
            return {"msg": "Please provide a valid email address"}

        elif re.match("^[a-zA-Z0-9_]*$", password):
            return {"msg": "Your password should have at least 1 capital letter, special character and number."}

        if password == confirm_password:
            self.user_dict['user_id'] = self.user_id
            self.user_dict['username'] = username
            self.user_dict['email'] = email
            self.user_dict['password'] = password

            Data.user_data.append(self.user_dict)
        else:
            return {"msg": "Passwords do not match. Try again."}
        return {"msg": "User created successfully.", "user_data": self.user_dict}

    @staticmethod
    def login_user(email, password):

        """
            Logs in user.
            Arguments:
                Email: Personal email of the user.
                Password: A secret security key.
        """

        for user in Data.user_data:
            if email == user['email']:
                if password == user['password']:
                    return {"msg": "Successfully logged in!"}
                return {"msg": "Wrong Password. Try again."}
        return {"msg": "You have no account,please sign up"}

    def reset_password(self, email, new_password, confirm_new_password):

        """
            Resets user's password.
            Arguments:
                Email: Personal email of the user.
                New Password: A secret security key.
        """

        for user in Data.user_data:
            if email == user['email']:
                if new_password == confirm_new_password:
                    self.user_dict['password'] = new_password
                    return {"message": "Your password has been reset"}

