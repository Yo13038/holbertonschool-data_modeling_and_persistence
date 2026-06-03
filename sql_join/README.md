SQL: Joins & Relationships
Introduction
In the previous project, you learned how to manipulate data within a single table using SQL. However, real-world systems rarely store all data in one place.

Instead, data is divided into multiple related tables, each representing a different entity (for example: users, products, orders).

In this project, you will learn how to:

model relationships between tables
understand how tables are connected using keys
combine data from multiple tables using joins
write more advanced queries using subqueries
This is a fundamental step toward working with real-world databases.

Learning Objectives
By the end of this project, you should be able to:

Understand relationships:

1–1, 1–N, N–N
Distinguish between:

primary key
foreign key
Understand referential integrity (conceptually)

Write queries using:

INNER JOIN
LEFT JOIN
CROSS JOIN
Interpret NULL values in joins

Work with junction tables

Use subqueries in filtering and comparisons

Resources
https://www.sqlite.org/lang_select.html
https://www.sqlite.org/foreignkeys.html
https://www.sqlite.org/lang_expr.html
https://www.w3schools.com/sql/sql_join.asp
Provided Files
You will be using the following dataset: library.db

Tables:
authors
id
name
country
books
id
title
author_id
price
students
id
name
courses
id
title
enrollments
student_id
course_id
General Requirements
Environment:

Ubuntu 20.04
SQLite 3.x
Each task:

must be a .sql file
must contain a single query (unless stated otherwise)
Execution:

sqlite3 library.db < file.sql
Output must:

match expected results exactly
include explicit ORDER BY when needed
Do not:

modify schema unless instructed
use unsupported SQL features
Important Notes
1. Join conditions are critical
A missing or incorrect ON condition can produce incorrect results.

2. NULL values
In outer joins:

missing matches → NULL
you must interpret them correctly
3. Relationships vs Queries
Relationships define structure
Joins reconstruct that structure in queries
4. SQLite behavior
Foreign keys may not be enforced unless enabled
Some SQL features differ from other databases
Always focus on writing logically correct SQL, not relying on engine-specific behavior.

SQLite does not support:

RIGHT JOIN
FULL OUTER JOIN
These can be simulated, but are not required in this project.

Final Remarks
This project introduces a key shift:

You are now working with connected data, not isolated tables.

Take time to understand:

how tables relate to each other
how joins reconstruct relationships
how queries reflect data structure
This understanding is essential before moving into database design and normalization.