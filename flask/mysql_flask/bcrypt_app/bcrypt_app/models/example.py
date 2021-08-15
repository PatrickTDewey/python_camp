from bcrypt_app.config.mysqlconnection import connectToMySQL
from bcrypt_app import app
from flask_bcrypt import Bcrypt
from flask import flash
import re

bcrypt = Bcrypt(app)

DATABASE = 'users_test_db'
USERNAME_REGEX = re.compile(r'^[a-zA-Z0-9]+$')


class User:
    def __init__(self, data):
        self.id = data['id']
        self.username = data['username']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (username, password, created_at, updated_at) VALUES (%(un)s, %(pw)s, NOW(), NOW())"
        print('saving data method....')
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_by_un(cls, data):
        query = 'SELECT * FROM users WHERE username = %(un)s;'
        username = connectToMySQL(DATABASE).query_db(query, data)
        if len(username) < 1:
            return False
        return cls(username[0])
    

    @staticmethod
    def validate_sign_up(data):
        is_valid = True
        # query = 'SELECT * FROM users WHERE username = %(un)s;'
        # username = connectToMySQL(DATABASE).query_db(query, data)
        if len(User.get_by_un(data)) >= 1:
            flash('username already taken, please select a different username')
            is_valid = False
        if not USERNAME_REGEX.match(data['un']):
            flash('please use only alpha numeric characters for username')
            is_valid = False
        if not data['conf']:
            flash('passwords don\'t match, please try again.')
            is_valid = False
        return is_valid
    @staticmethod
    def validate_login(data):
        is_valid = True
        user = User.get_by_un(data)
        if not user:
            flash('Invalid Username/Password')
            is_valid = False
        elif not bcrypt.check_password_hash(user.password, data['pw']): # if not true
            flash('Invalid Username/Password')
            is_valid = False
        return is_valid
