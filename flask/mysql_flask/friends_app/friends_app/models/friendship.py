from friends_app.config.mysqlcontroller import connectToMySQL
from friends_app import app
DATABASE = 'friendsDB'
class Friendship:
    def __init__(self, data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.friend_id = data['friend_id']

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO friendships(created_at, updated_at, user_id, friend_id) VALUES (NOW(), NOW(), %(user_id)s, %(friend_id)s);'
        return connectToMySQL(DATABASE).query_db(query,data)
    @classmethod
    def get_all_friends(cls):
        query = "SELECT users.first_name as user, friend.first_name as friend FROM users JOIN friendships ON users.id = friendships.user_id JOIN users as friend on friendships.friend_id = friend.id;"
        result = connectToMySQL(DATABASE).query_db(query)
        if not result:
            return False
        return result
        
    def __repr__(self):
        rep = f"created_at: {self.created_at}, updated_at: {self.updated_at}, user_id: {self.user_id}, friend_id: {self.friend_id}"
        return rep

