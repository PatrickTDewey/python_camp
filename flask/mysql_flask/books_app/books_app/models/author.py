# Import the function that will return an instance of a connection
from books_app.config.mysqlconnection import connectToMySQL
from books_app.models import book
DATABASE = "booksDB"
# Model the class after the friend table from our database
class Author:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.favorite_books = []

    # Now we use class methods to query our database

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL(DATABASE).query_db(query)
        authors = []
        for result in results:
            authors.append(cls(result))
        return authors
    @classmethod
    def get_authors_favorite_books(cls, data):
        query = "SELECT * FROM authors LEFT JOIN author_has_favorite_book ON authors.id = author_has_favorite_book.author_id LEFT JOIN books ON books.id = author_has_favorite_book.book_id WHERE authors.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        this_author = cls(results[0])
        for result in results:
            print(result)
            favorite_book = {
                "id": result["books.id"],
                "title": result["title"],
                "page_num":result["page_num"],
                "created_at": result["books.created_at"],
                "updated_at": result["books.updated_at"],
            }
            # if favorite_book not in this_author.favorite_books:
            #     print('True')
            this_author.favorite_books.append(book.Book(favorite_book))
            # else:
            #     print('False')
        
        return this_author
    @classmethod
    def add_to_favorites(cls, data):
        query = "INSERT INTO author_has_favorite_book(book_id, author_id) VALUES (%(bid)s,%(aid)s)"
        return connectToMySQL(DATABASE).query_db(query, data)
    @classmethod
    def get_author(cls, data):
        # result = []
        query = "SELECT id FROM authors WHERE first_name = %(fname)s"
        result = connectToMySQL(DATABASE).query_db(query,data)
        print(result)
        # return result[0]['id']
    @classmethod
    def save(cls, data):
        query = "INSERT INTO authors (first_name, last_name, created_at, updated_at) VALUES (%(fname)s, %(lname)s, NOW(), NOW());"
        return connectToMySQL(DATABASE).query_db(query, data)
    @classmethod
    def get_info(cls, data):
        query = "SELECT * FROM authors WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def update(cls, data):
        query = "UPDATE authors SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s, updated_at = NOW() WHERE id= %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM authors WHERE id = %(author_id)s"
        return connectToMySQL(DATABASE).query_db(query, data)
    def __repr__(self):
        return f"id: {self.id}, first_name: {self.first_name}, last_name: {self.last_name} created_at: {self.created_at}, updated_at: {self.updated_at}\n"