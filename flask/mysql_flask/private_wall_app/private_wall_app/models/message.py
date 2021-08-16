from private_wall_app.config.mysqlconnection import connectToMySQL
from private_wall_app.models import user
from private_wall_app import app
from flask_bcrypt import bcrypt
from flask import flash

DATABASE = 'private_wall_db'

class Message:
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user2_id = data['user2_id']


    @classmethod
    def save(cls, data):
        query = 'INSERT INTO messages(content, created_at, updated_at, user_id, user2_id) VALUES (%(content)s, NOW(), NOW(), %(id)s, %(sent_by)s);'
        return connectToMySQL(DATABASE).query_db(query, data)
    @classmethod
    def get_by_id(cls, data):
       return connectToMySQL(DATABASE).query_db(query, data)

    def __repr__(self):
        rep = f'{self.id}, {self.content}, sent to: {self.user_id}, sent_by: {self.user2_id}'
        return rep
