# Overview

I created a very small movie database that holds movie information like the title, the year it was shown in theaters, and the genre that it's in. Although still in development, I'd like for the data to be displayed by year and genre. Possibly even by a specific letter sequence when it's queried in a search bar.

I wanted to experiment with a new database program. I have had experience with mySQL, Postgres, and MongoDB so I wanted to use something different to see what I could learn. I found that it's very similar to using other databases which I like because it shows that the development is consistent. I did learn quite a bit on how to connect the database through the sqlite3 package and allowing python to create the tables, as well as integrate the data.


[Software Demo Video](https://cdnapisec.kaltura.com/index.php/extwidget/preview/partner_id/1157612/uiconf_id/42438192/entry_id/1_mw0zkj0k/embed/dynamic)

# Relational Database

## Movie 
- Title
- Release Year
- Genre

## Actor
- Actor ID
- Actor Name

## Actors by Movie
- Movie ID
- Actor ID

# Development Environment
- Python
- SQLite package for Python
- SQLiteStudio V3.4.4
- Visual Studio Code
- Github Repository

# Useful Websites

- [SQLite - Python](https://www.tutorialspoint.com/sqlite/sqlite_python.htm)
- [Tutorial to Install](https://www.sqlitetutorial.net/)

# Future Work

- A function that checks if a value (movie or actor) already exists so it doesn't duplicate data
- Adding more table like director names so that it can display movies by directors