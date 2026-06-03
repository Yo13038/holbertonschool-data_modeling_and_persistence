SELECT books.title AS title, authors.name AS authors_name
FROM books
INNER JOIN authors 
ON books.author_id = authors.id
ORDER BY ASC title;
