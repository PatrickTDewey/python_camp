from user_recipes_app.config.mysqlconnection import connectToMySQL
from user_recipes_app.models import user
from flask import flash


DATABASE = 'recipeDB'


class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.under_30 = data['under_30']
        self.instructions = data['instructions']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def get_all(cls, data):
        query = 'SELECT * FROM recipes;'
        print('Getting all recipes...')
        results = connectToMySQL(DATABASE).query_db(query)
        recipes = []
        for row in results:
            recipes.append(cls(row))
        return recipes
    @classmethod
    def get_other_recipes(cls, data):
       query = 'SELECT * FROM recipes WHERE recipes.id NOT IN ( SELECT recipe_id FROM user_has_recipes WHERE user_id = %(id)s);'
       results = connectToMySQL(DATABASE).query_db(query, data)
       recipes = []
       for row in results:
           recipes.append(cls(row))
       print(recipes)   
       return recipes

    @ classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name, description, under_30, instructions, created_at, updated_at) VALUES(%(name)s, %(desc)s, %(under_30)s, %(instructions)s, %(created_at)s, NOW());"
        return connectToMySQL(DATABASE).query_db(query, data)
    @classmethod
    def add_recipe_to_user(cls, data):
        query = 'INSERT INTO user_has_recipes (user_id, recipe_id) VALUES (%(user_id)s, %(recipe_id)s);'
        return connectToMySQL(DATABASE).query_db(query, data)
    @classmethod
    def view(cls, data):
        query = 'SELECT * FROM recipes WHERE recipes.id = %(recipe_id)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        recipe = cls(results[0])
        return recipe
    @classmethod
    def update(cls, data):
        query = 'UPDATE recipes SET name = %(name)s, description = %(desc)s, under_30 = %(under_30)s, instructions = %(instructions)s, updated_at = %(date_updated)s WHERE recipes.id = %(id)s;'
        return connectToMySQL(DATABASE).query_db(query, data)
    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM user_has_recipes WHERE recipes.id = %(recipe_id)s;'
        return connectToMySQL(DATABASE).query_db(query,data)
    # @classmethod
    # def can_edit():
    #     pass
    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len(data['name']) == 0:
            flash('Name is a required field', 'name')
            is_valid = False
        if len(data['desc']) == 0:
            flash('Description is a required field', 'description')
            is_valid = False
        if len(data['instructions']) == 0:
            flash('Instructions is a required field.', 'instructions')
            is_valid = False
        if len(data['name']) < 3:
            flash('Fields must be atleast 3 characters long.', 'name')
            is_valid = False
        if len(data['desc']) < 3:
            flash('Fields must be atleast 3 characters long.', 'description')
            is_valid = False
        if len(data['instructions']) < 3:
            flash('Fields must be atleast 3 characters long.', 'instructions')
            is_valid = False
        return is_valid
    def __repr__(self):
        rep = f"ID: {self.id}, Name: {self.name}, Description: {self.description}, under_30: {self.under_30} Instruction: {self.instructions}, CA: {self.created_at}, UA: {self.updated_at}"
        return rep
