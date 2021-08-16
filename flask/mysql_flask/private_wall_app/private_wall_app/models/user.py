from private_wall_app.config.mysqlconnection import connectToMySQL
from private_wall_app.models import message
from private_wall_app import app
from flask_bcrypt import Bcrypt
from flask import flash
import re

bcrypt = Bcrypt(app)

DATABASE = 'private_wall_db'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# between 6 - 20 characters, one capital number, one special character, one number
PASSWORD_REGEX = re.compile(
    "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$")


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.messages = []

    @classmethod
    def get_all(cls, data):
        query = 'SELECT * FROM users;'
        print('Getting all users...')
        results = connectToMySQL(DATABASE).query_db(query)
        all_users = []
        for result in results:
            all_users.append(cls(result))
        return all_users

    @classmethod
    def get_user_messages(cls, data):
        # make_user = cls.get_by_id(data)
        # query = "SELECT users.first_name as 'sent to' , messages.content, users2.first_name as 'sent_from' FROM users JOIN messages ON users.id = messages.user_id JOIN users as users2 ON users2.id = messages.user2_id WHERE users.id = %(id)s;"
        query = "SELECT * FROM users LEFT JOIN messages on users.id = messages.user_id WHERE users.id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        user = cls(results[0])
        
        for result in results:
        #    print(result)
        #    make_user.messages.append(result)
            new_message = {
                'id': result['messages.id'],
                'content': result['content'],
                'created_at': result['messages.created_at'],
                'updated_at': result['messages.updated_at'],
                'user_id': result['user_id'],
                'user2_id': result['user2_id']
            }
            data = {
                'id': result['user2_id']
            }
            if result['content'] != None:
                user.messages.append([message.Message(new_message), User.get_by_id(data)])
        print(user)
        return user
    def get_sent_by(cls, data):
        query='SELECT ALL FROM USERS WHERE '
        pass
    @ classmethod
    def get_other_users(cls, data):
        query='SELECT * FROM users WHERE id NOT LIKE %(id)s;'
        results=connectToMySQL(DATABASE).query_db(query, data)
        other_users=[]
        if not results:  # catch for if there are no
            return False
        else:
            for result in results:
                other_users.append(cls(result))
        return other_users
    @ classmethod
    def save(cls, data):
        query="INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES(%(fn)s, %(ln)s, %(email)s,%(pw)s, NOW(), NOW());"
        return connectToMySQL(DATABASE).query_db(query, data)

    @ classmethod
    def get_by_email(cls, data):
        query='SELECT * FROM users WHERE email = %(email)s'
        email=connectToMySQL(DATABASE).query_db(query, data)
        if len(email) < 1:
            return False
        user=cls(email[0])
        return user

    @ classmethod
    def get_by_id(cls, data):
        query='SELECT * FROM users WHERE id = %(id)s'
        user=connectToMySQL(DATABASE).query_db(query, data)
        return cls(user[0])

    @ staticmethod
    def validate_registration(data):
        is_valid=True
        if User.get_by_email(data):
            flash('Email is taken already, please choose a different email.', 'email')
            is_valid=False
        if not EMAIL_REGEX.match(data['email']):
            flash('Please enter a valid format for your email address', 'email')
            is_valid=False
        if not data['fn'].isalpha() or len(data['fn']) < 2:
            flash('First name must include only alphabetic characters and be atleast 2 characters long.', 'first_name')
            is_valid=False
        if not data['ln'].isalpha() or len(data['ln']) < 2:
            flash('Last name must include only alphabetic characters and be atleast 2 characters long.', 'last_name')
            is_valid=False
        if data['pw_length'] < 8:
            flash('Password must be atleast 8 characters long', 'password')
        if not data['pw_check']:
            flash('Passwords are not matching, please try again.', 'password')
            is_valid=False
        if not PASSWORD_REGEX.match(data['re']):
            flash('Password must contain atleast one capital letter, one special character, and one number', 'password')
        return is_valid
    @ staticmethod
    def validate_login(data):
        is_valid=True
        user=User.get_by_email(data)
        if not user:
            print('Email didn\'t exist')
            flash('Invalid Email/Password.', 'error')
            is_valid=False
        elif not bcrypt.check_password_hash(user.password, data['pw']):
            print('Password did not match stored password')
            flash('Invalid Email/Password.', 'error')
            is_valid=False
        return is_valid

    def __repr__(self):
        rep=f"{self.id}, {self.first_name}, {self.last_name}, {self.created_at}, {self.updated_at}, {self.messages}"
        return rep
