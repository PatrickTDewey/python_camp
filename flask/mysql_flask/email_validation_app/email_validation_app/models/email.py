from email_validation_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
DATABASE = "email_validDB"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class Email:
    def __init__(self, data):
        self.id = data["id"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL(DATABASE).query_db(query)
        emails = []
        for result in results:
            emails.append(cls(result))

        print(emails)
        for email in emails:
            print (email.id)
        return emails
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES( %(email_address)s, NOW(),NOW());"
        return connectToMySQL(DATABASE).query_db(query, data)
    @staticmethod
    def validate_email(form):
        is_valid = True

        if not EMAIL_REGEX.match(form["email_address"]):
            flash("Please enter a valid email address")
            is_valid = False

        return is_valid

    