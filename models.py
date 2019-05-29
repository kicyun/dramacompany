import sqlite3 as sql

def insertUser(email,password,is_driver):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (email,password,is_driver) VALUES (?,?,?)", (email,password,is_driver))
    con.commit()
    con.close()

def selectUser(email):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT email,password,is_driver  FROM users email = (?)", [email])
    user = cur.fetchone()
    con.close()
    return user
