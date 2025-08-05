import sqlite3

def connect():
    return sqlite3.connect("Database.db")

def table():
    conn = connect()
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS data(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    phone_num TEXT NOT NULL
    )''')
    conn.commit()
    conn.close()

def insert_data(username, phone_num):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO data(username,phone_num) VALUES(?,?)", (username,phone_num))
    conn.commit()
    conn.close()
    print(username, phone_num)

table()