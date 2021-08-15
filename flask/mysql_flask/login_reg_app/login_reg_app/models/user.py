from login_reg_app.config.mysqlconnection import connectToMySQL
from login_reg_app import app
from flask_bcrypt import Bcrypt
from flask import flash
import re

bcrypt = Bcrypt(app)

DATABASE = 'user_login_db'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

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
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES(%(fn)s, %(ln)s, %(email)s,%(pw)s, NOW(), NOW());"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_by_email(cls, data):
        query = 'SELECT * FROM users WHERE email = %(email)s'
        email = connectToMySQL(DATABASE).query_db(query, data)
        if len(email) < 1:
            return False
        return cls(email[0])

    @classmethod
    def get_by_id(cls, data):
        query = 'SELECT * FROM users WHERE id = %(id)s'
        user = connectToMySQL(DATABASE).query_db(query, data)
        return cls(user[0])
    
    @staticmethod
    def validate_registration(data):
        is_valid = True
        if User.get_by_email(data):
            flash('Email is taken already, please choose a different email.', 'email')
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash('Please enter a valid format for your email address', 'email')
            is_valid = False
        if not data['fn'].isalpha() or len(data['fn']) < 2:
            flash('First name must include only alphabetic characters and be atleast 2 characters long.', 'first_name')
            is_valid = False
        if not data['ln'].isalpha() or len(data['ln']) < 2:
            flash('Last name must include only alphabetic characters and be atleast 2 characters long.', 'last_name')
            is_valid = False
        if data['pw_length'] < 8:
            flash('Password must be atleast 8 characters long', 'password')
        if not data['pw_check']:
            flash('Passwords are not matching, please try again.', 'password')
            is_valid = False
        return is_valid
    @staticmethod
    def validate_login(data):
        is_valid = True
        user = User.get_by_email(data)
        if not user:
            print('Email didn\'t exist')
            flash('Invalid Email/Password.', 'error')
            is_valid = False
        elif not bcrypt.check_password_hash(user.password, data['pw']):
            print('Password did not match stored password')
            flash('Invalid Email/Password.', 'error')
            is_valid = False
        return is_valid

        