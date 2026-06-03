SELECT books.title AS title, authors.name AS authors_name
FROM books
JOIN authors 
ON books.author_id = authors.id