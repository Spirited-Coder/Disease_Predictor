import sqlite3
try:
    con = sqlite3.connect('users.db')
    print("Connection Successful")

    cursor = con.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL)
                ''')
    print("Table created successfully")

except sqlite3.Error as error:
    print("Error while connecting to database. ",error)

finally:
    if con:
        con.close()
        print("Database closed.")