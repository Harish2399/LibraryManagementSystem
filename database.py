import sqlite3

connection = sqlite3.connect("library.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books(

book_id TEXT PRIMARY KEY,
book_name TEXT,
author TEXT,
status TEXT,
student TEXT

)
""")

connection.commit()

connection.close()

print("Database Created Successfully")