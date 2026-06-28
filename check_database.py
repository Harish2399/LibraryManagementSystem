import sqlite3

connection = sqlite3.connect("library.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM books")

rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()