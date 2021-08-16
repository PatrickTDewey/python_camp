from user_recipes_app.config.mysqlconnection import connectToMySQL
from user_recipes_app.models import recipe
from user_recipes_app import app
from flask_bcrypt import Bcrypt
from flask import flash
import re

bcrypt = Bcrypt(app)

DATABASE = 'recipeDB'
# email regex password
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
        self.pw = data['pw']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.recipes = []

    @classmethod
    def get_all(cls, data):
        query = 'SELECT * FROM users;'
        print('Getting all users...')
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, pw, created_at, updated_at) VALUES(%(fn)s, %(ln)s, %(email)s,%(pw)s, NOW(), NOW());"
        return connectToMySQL(DATABASE).query_db(query, data)

    

    @ classmethod
    def get_by_id(cls, data):
        query = 'SELECT * FROM users LEFT JOIN user_has_recipes ON users.id = user_has_recipes.user_id LEFT JOIN recipes ON recipes.id = user_has_recipes.recipe_id WHERE users.id = %(id)s'
        results = connectToMySQL(DATABASE).query_db(query, data)
        user = cls(results[0])
        for row in results:
            if row['recipes.id'] == None:
                break
            data = {
                'id': row['recipes.id'],
                'name': row['name'],
                'description': row['description'],
                'under_30': row['under_30'],
                'instructions': row['instructions'],
                'created_at': row['recipes.created_at'],
                'updated_at': row['recipes.updated_at']
            }
            user.recipes.append(recipe.Recipe(data))
        for j in user.recipes:
            print(j)
        return user
    @ classmethod
    def get_by_email(cls, data):
        query='SELECT * FROM users WHERE email = %(email)s'
        email=connectToMySQL(DATABASE).query_db(query, data)
        if len(email) < 1:
            return False
        user=cls(email[0])
        return user

    @ staticmethod
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
        if not PASSWORD_REGEX.match(data['re']):
            flash('Password must contain atleast one capital letter, one special character, and one number', 'password')
        return is_valid

    @ staticmethod
    def validate_login(data):
        is_valid = True
        user = User.get_by_email(data)
        if not user:
            print('Email didn\'t exist')
            flash('Invalid Email/Password.', 'error')
            is_valid = False
        elif not bcrypt.check_password_hash(user.pw, data['pw']):
            print('Password did not match stored password')
            flash('Invalid Email/Password.', 'error')
            is_valid = False
        return is_valid

    def __repr__(self):
        rep = f"ID: {self.id}, FN: {self.first_name}, LN: {self.last_name}, CA: {self.created_at}, UA: {self.updated_at}, Recipes: {self.recipes}"
        return rep
