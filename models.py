import sqlite3 as sql

def insertUser(email,password,is_driver):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (email,password,is_driver) VALUES (?,?,?)", (email,password,is_driver))
    con.commit()
    con.close()

def selectUserByEmail(email):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT id, email,password,is_driver FROM users email = ?", email)
    user = cur.fetchone()
    con.close()
    return user

def selectUserById(user_id):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT id, email,password,is_driver FROM users id = ?", user_id)
    user = cur.fetchone()
    con.close()
    return user

def insertRequest(passenger, address):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO requests (passenger, address) VALUES (?)", (passenger, address))
    con.commit()
    con.close()

def updateRequest(request_id, driver):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("UPDATE requests SET driver = ?, dispatch_time = ? WHERE id = ?", (driver, datetime('now', 'localtime'), request_id)
    con.commit()
    con.close()

def selectRequestList():
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT id, passenger, address, driver, request_time, dispatch_time FROM users ORDER BY id DESC")
    user = cur.fetchone()
    con.close()
    return user

def selectRequestById(request_id):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT id, passenger, address, driver, request_time, dispatch_time FROM users WHERE id = ?", request_id)
    user = cur.fetchone()
    con.close()
    return user
