import sqlite3

def connect_database():
    return sqlite3.connect("ams_student_database.db")

def create_table():
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS student_data(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
    )''')
    conn.commit()
    conn.close()

def insert_data(username, password):
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO student_data(username,password) VALUES(?,?)", (username,password))
    conn.commit()
    conn.close()
    print(username, password)

create_table()