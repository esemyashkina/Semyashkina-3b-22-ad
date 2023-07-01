import sqlite3

conn = sqlite3.connect('books.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS movies
(id INTEGER PRIMARY KEY, name TEXT, genre TEXT, rating REAL)''')

movies_data = [('Alvin and the Chipmunks', 'comedy', 6.8),
              ('Titanic', 'drama', 8.9),
              ('Midsommar', 'drama', 7.5)]

cursor.executemany("INSERT INTO movies (name, genre, rating) VALUES (?, ?, ?)", movies_data)

conn.commit()

cursor.execute('SELECT * FROM movies WHERE genre = "drama"')
rows = cursor.fetchall()

for row in rows:
    print(f'Name: {row[1]}, genre: {row[2]}, rating: {row[3]}')

conn.close()
