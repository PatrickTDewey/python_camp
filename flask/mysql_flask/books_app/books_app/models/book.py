# Import the function that will return an instance of a connection
from books_app.config.mysqlconnection import connectToMySQL
from books_app.models import author
DATABASE = "booksDB"
# Model the class after the friend table from our database


class Book:
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.page_num = data["page_num"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.favorite_authors = []
    # Now we use class methods to query our database

    @classmethod
    def get_books_favorite_authors(cls, data):
        query = "SELECT * FROM books LEFT JOIN author_has_favorite_book ON books.id = author_has_favorite_book.book_id LEFT JOIN authors ON authors.id = author_has_favorite_book.author_id WHERE books.id = %(id)s;"
        
        results = connectToMySQL(DATABASE).query_db(query, data)
        this_book = cls(results[0])
        for result in results:
            print(result)
            favorite_author = {
                "id": result["authors.id"],
                "first_name": result["first_name"],
                "last_name": result["last_name"],
                "created_at": result["authors.created_at"],
                "updated_at": result["authors.updated_at"],
            }
            this_book.favorite_authors.append(author.Author(favorite_author))
        return this_book
    @classmethod
    def add_author(cls, data):
        query = "INSERT INTO author_has_favorite_book(book_id, author_id) VALUES (%(bid)s,%(aid)s)"
        return connectToMySQL(DATABASE).query_db(query, data)
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL(DATABASE).query_db(query)
        books = []
        for result in results:
            books.append(cls(result))
        return books

    @classmethod
    def get_by_id(cls, data):
        result = []
        query = "SELECT id FROM books WHERE title = %(title)s"
        result = connectToMySQL(DATABASE).query_db(query, data)
        print(result)
        return result[0]['id']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO books (title, page_num, created_at, updated_at) VALUES (%(title)s, %(pnum)s, NOW(), NOW());"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_info(cls, data):
        query = "SELECT * FROM books WHERE id = %(book_id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE books SET title = %(title)s, page_num = %(page_num)s updated_at = NOW() WHERE id= %(book_id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM books WHERE id = %(book_id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

    def __repr__(self):
        return f"id: {self.id}, title: {self.title}, created_at: {self.created_at}, updated_at: {self.updated_at}\n"
