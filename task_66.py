import sqlite3

conn = sqlite3.connect('student.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students
(id INTEGER PRIMARY KEY, name TEXT, age INTEGER, average_score REAL)''')

students_data = [('John', 13, 3.5),
                 ('Anna', 15, 4.2),
                 ('Ted', 14, 4.8)]

cursor.executemany("INSERT INTO students (name, age, average_score) VALUES (?, ?, ?)", students_data)

conn.commit()

cursor.execute('SELECT * FROM students')
rows = cursor.fetchall()

for row in rows:
    print(f'Name: {row[1]}, Age: {row[2]}, Average Score: {row[3]}')

conn.close()
