# Import the function that will return an instance of a connection
from dojo_survey_app.config.mysqlconnection import connectToMySQL
from flask import flash
DATABASE = "dojo_survey_db"

class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.language = data["language"]
        self.comment = data["comment"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    # Now we use class methods to query our database
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for result in results:
            dojos.append(cls(result))
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, location, language, comment, created_at, updated_at) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_info(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE dojos SET name = %(name)s, location = %(location)s, language = %(language)s, comment = %(comment)s   updated_at = NOW() WHERE id= %(dojo_id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM dojos WHERE id = %(dojo_id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate_survey(survey):
        is_valid = True # we assume this is true
        if not survey['name']:
            print("Name is empty..add a name")
            flash("Name is Empty...Try adding a name")
            is_valid = False
        if not survey['location']:
            print("location is empty..add a location")
            flash("location is Empty...Try adding a location")
            is_valid = False
        if not survey['language']:
            print("lanugage is empty..add a language")
            flash("lanugage is Empty...Try adding a language")
            is_valid = False
        if not survey['comment']:
            print("comment is empty..add a comment")
            flash("comment is Empty...Try adding a comment")
            is_valid = False
        return is_valid


    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, location: {self.location}, language: {self.language}, comment: {self.comment}, created_at: {self.created_at}, updated_at: {self.updated_at}\n"
