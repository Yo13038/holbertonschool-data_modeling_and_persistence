Introduction
In the relational model, a table is the fundamental structure used to store data.

Each table is defined by:

a name
a set of columns
a type associated to each column
Before you can insert or query data, the database must know how the data is structured. This is done using the CREATE TABLE statement.

This task focuses on understanding:

how a table is defined
how columns are declared
how basic constraints influence the structure of the data
Even though SQLite is flexible with types, you should aim to define a clear and consistent schema, as would be required in stricter database systems.

Context
You are working on a simple data system that stores information about books.

Your goal is to define a table named:

books
This table will be used in all subsequent tasks of the project.

Getting Started with SQLite
Before creating your table, you need to work inside a database.

In this project, you will use SQLite, which stores the entire database in a single file.

Creating a new database
To create and open a new SQLite database, run:

sqlite3 my_database.db
If the file my_database.db does not exist, SQLite will create it automatically.

Once inside the SQLite prompt, you can execute SQL statements directly. Use .help to get info about the available SQLite commands.

Also you can run your .sql file from the shell using:

sqlite3 my_database.db < 0-create_table.sql
This will execute all the SQL statements contained in your file.