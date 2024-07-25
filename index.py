import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('movie_database0.sqlite')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies (
        movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        release_year INTEGER,
        genre TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS actors (
        actor_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS movie_actors (
        movie_id INTEGER,
        actor_id INTEGER,
        FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
        FOREIGN KEY (actor_id) REFERENCES actors(actor_id),
        PRIMARY KEY (movie_id, actor_id)
    )
''')

conn.commit()

# Function to add a new movie to the database
def add_movie(title, release_year, genre):
    sql = "INSERT INTO movies (title, release_year, genre) VALUES (?, ?, ?)"
    cursor.execute(sql, (title, release_year, genre))
    conn.commit()
    return cursor.lastrowid

# Function to update movie details
def update_movie(movie_id, title=None, release_year=None, genre=None):
    update_fields = []
    params = []
    
    if title:
        update_fields.append("title = ?")
        params.append(title)
    if release_year:
        update_fields.append("release_year = ?")
        params.append(release_year)
    if genre:
        update_fields.append("genre = ?")
        params.append(genre)
    
    params.append(movie_id)
    
    sql = "UPDATE movies SET " + ", ".join(update_fields) + " WHERE movie_id = ?"
    cursor.execute(sql, params)
    conn.commit()
    return cursor.rowcount > 0

# Function to delete a movie by its ID
def delete_movie(movie_id):
    sql = "DELETE FROM movies WHERE movie_id = ?"
    cursor.execute(sql, (movie_id,))
    conn.commit()
    return cursor.rowcount > 0


# Function to add an actor to the database
def add_actor(name):
    sql = "INSERT INTO actors (name) VALUES (?)"
    cursor.execute(sql, (name,))
    conn.commit()
    return cursor.lastrowid

# Function to update actor in database from database by id
def update_actor(actor_id):
    sql = "UPDATE INTO actors where actor_id = ?"
    cursor.execute(sql, (actor_id,))
    conn.commit()
    return cursor.lastrowid

# Function to delete actor from database by id
def delete_actor(actor_id):
    sql = "DELETE FROM actors where actor_id = ?"
    cursor.execute(sql, (actor_id,))
    conn.commit()
    return cursor.lastrowid


# Function to associate an actor with a movie
def add_actor_to_movie(movie_id, actor_id):
    sql = "INSERT INTO movie_actors (movie_id, actor_id) VALUES (?, ?)"
    cursor.execute(sql, (movie_id, actor_id))
    conn.commit()

# Function to retrieve a movie with its actors
def get_movie_with_actors(movie_id):
    sql = """
        SELECT m.movie_id, m.title, m.release_year, m.genre, GROUP_CONCAT(a.name, ', ')
        FROM movies m
        LEFT JOIN movie_actors ma ON m.movie_id = ma.movie_id
        LEFT JOIN actors a ON ma.actor_id = a.actor_id
        WHERE m.movie_id = ?
        GROUP BY m.movie_id
    """
    cursor.execute(sql, (movie_id,))
    return cursor.fetchone()

# Example usage
if __name__ == "__main__":
    # Add a movie
    # movie_id = add_movie("Extraction", 2020, "Action")
    # movie_id1 = add_movie("Bullet Train", 2022, "Action")
    # movie_id2 = add_movie("Snake Eyes", 2021, "Action")
    # movie_id3 = add_movie("Atonement", 2007, "Romance")
    # movie_id4 = add_movie("500 Days Of Summer", 2009, "Romance")
    # movie_id5 = add_movie("Malcom and Marie", 2021, "Romance")
    
    # # Add actors
    # actor1_id = add_actor("Chris Hemsworth") #Extraction
    # actor2_id = add_actor("Rudhraksh Jaiswal") #Extraction

    # actor3_id = add_actor("Brad Pitt") #Bullet Train
    # actor4_id = add_actor("Joey King") #Bullet Train

    # actor5_id = add_actor("Henry Golding") #Snake Eyes
    # actor6_id = add_actor("Andrew Koji") #Snake Eyes

    # actor7_id = add_actor("Joseph Gordon-Levitt") #500
    # actor8_id = add_actor("Zooey Deschanel") #500
    
    # actor9_id = add_actor("Chris Hemsworth") #Malcom & Marie
    # actor10_id = add_actor("Rudhraksh Jaiswal") #Malcom & Marie

    # actor11_id = add_actor("Keira Knightley") #Atonement
    # actor12_id = add_actor("James McAvoy") #Atonement
  
    
    # # Delete actors by id
    # actor1_id = delete_actor(2)
    
    # Associate actors with the movie
    # add_actor_to_movie(56, 109)
    # add_actor_to_movie(56, 110)

    # Retrieve and print the movie with actors
    # movie = get_movie_with_actors(56)
    # print("Retrieved movie with actors:", movie)
    
    # # Update the movie
    #update_result = update_movie(56, title="Extraction")
    #print("Movie updated:", update_result)
    
    # # Delete the movie
    delete_result = delete_movie(56)
    print("Movie deleted:", delete_result)