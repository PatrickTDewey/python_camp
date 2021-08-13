USE booksDB;
INSERT INTO authors(first_name, last_name, created_at, updated_at)
VALUES ("Ernest", "Hemingway", NOW(),NOW()), ("Walt", "Whitman", NOW(), NOW()), ("J.R", "Tolken", NOW(), NOW());
SELECT * FROM authors;

INSERT INTO books(title, page_num, created_at, updated_at)
VALUES("Harry Potter", 321, NOW(), NOW()), ("Where the red fern grows", 180, NOW(), NOW()),("The Lord Of The Rings", 613, NOW(), NOW());

SELECT * FROM authors WHERE id = 1;
INSERT INTO author_has_favorite_book(book_id, author_id)
VALUES (1,3),(2,1);

SELECT * FROM authors LEFT JOIN author_has_favorite_book ON authors.id = author_has_favorite_book.author_id
LEFT JOIN author_has_favorite_book ON books.id = author_has_favorite_book.book_id;



SELECT * FROM authors JOIN author_has_favorite_book ON authors.id = author_has_favorite_book.author_id JOIN books ON books.id = author_has_favorite_book.book_id WHERE authors.id = 1;
SELECT * FROM books JOIN author_has_favorite_book ON books.id = author_has_favorite_book.book_id JOIN authors ON authors.id = author_has_favorite_book.author_id WHERE books.id = 1;

SELECT * FROM books LEFT JOIN author_has_favorite_book ON books.id = author_has_favorite_book.book_id LEFT JOIN authors ON authors.id = author_has_favorite_book.author_id WHERE books.id = 1;
SELECT * FROM authors JOIN author_has_favorite_book ON authors.id = author_has_favorite_book.author_id JOIN books ON books.id = author_has_favorite_book.book_id WHERE book.id = 1;