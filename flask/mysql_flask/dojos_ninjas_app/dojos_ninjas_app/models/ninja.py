# Import the function that will return an instance of a connection
from dojos_ninjas_app.config.mysqlconnection import connectToMySQL

DATABASE = "dojo_ninjas"
# Model the class after the friend table from our database
class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.dojo_id = data["dojo_id"]
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(DATABASE).query_db(query)
        ninjas = []
        for result in results:
            ninjas.append(cls(result))
        return ninjas
    @classmethod
    def get_by_id(cls, data):
        result = []
        query = "SELECT id FROM ninjas WHERE first_name = %(fname)s AND last_name = %(lname)s"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result[0]['id']
    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) VALUES (%(fname)s, %(lname)s, %(age)s, NOW(), NOW(), %(dojo_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    @classmethod
    def get_info(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    @classmethod
    def update(cls, data):
        query = "UPDATE ninjas SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s, updated_at = NOW() WHERE id= %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM ninjas WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)
    def __repr__(self):
        return f"id: {self.id}, first_name: {self.first_name}, last_name: {self.last_name}, email: {self.email}, created_at {self.created_at}, updated_at: {self.updated_at}\n"