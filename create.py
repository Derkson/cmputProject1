import sqlite3
import random
from datetime import date
import validation
global conn, c
path = './miniproject1.db'
conn = sqlite3.connect(path)
c = conn.cursor()
c.execute(' PRAGMA foreign_keys=ON ')

def make_regno(table):
    regno = random.randint(1,1000)
    if(table ==  "births"):
        c.execute('SELECT regno FROM births;')
    elif(table == "marriages"):
        c.execute('SELECT regno FROM marriages;')
    elif(table == "vehicles"):
        c.execute('SELECT regno FROM registrations')
    else:
        return -1

    rows = c.fetchall()
    for (x,) in rows:
        if(x == regno):
            return make_regno(table)

def create_person(fname, lname, bdate, bplace, address, phone):
    insertions = (fname, lname, bdate, bplace, address, phone)
    c.execute('INSERT INTO persons VALUES(?,?,?,?,?,?);',insertions)
    conn.commit()

def create_birth(regno, fname, lname, regdate, regplace, gender, f_fname, f_lname, m_fname, m_lname):
    insertions = (regno, fname, lname, regdate, regplace, gender, f_fname,f_lname, m_fname, m_lname)
    c.execute('INSERT INTO births VALUES(?,?,?,?,?,?,?,?,?,?);', insertions)
    conn.commit()

def create_marriage(regno, regdate, regplace, p1_fname, p1_lname, p2_fname, p2_lname):
    insertions = (regno, regdate, regplace, p1_fname, p2_lname, p2_fname, p2_lname)
    c.execute('INSERT INTO marriages VALUES(?,?,?,?,?,?,?);', insertions)
    conn.commit()

def create_registration(regno, regdate, expiry, plate, vin, fname, lname):
    insertions = (regno, regdate, expiry, plate, vin, fname, lname)
    c.execute('INSERT INTO registrations VALUES(?,?,?,?,?,?,?);', insertions)
    conn.commit()

def create_payment(tno, pdate, amount):
    insertions = (tno, pdate, amount)
    c.execute("INSERT INTO payments VALUES(?,?,?)", insertions)
    conn.commit()

def get_city_of_user(uid):
    c.execute('''SELECT city
                 FROM users
                 WHERE uid=:userID;''',
                 {"userID":uid})

    city = c.fetchone()
    return city[0]
