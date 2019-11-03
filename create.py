import sqlite3
import random
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
    elif(table == "tickets"):
        c.execute('SELECT tno FROM tickets')
    else:
        return -1

    rows = c.fetchall()
    for (x,) in rows:
        if(x == regno):
            return make_regno(table)

def create_person(fname, lname, bdate, bplace, address, phone):
    insertions = (fname, lname, bdate, bplace, address, phone)
    c.execute('INSERT INTO persons VALUES(?,?,?,?,?,?);',insertions)

def create_birth(regno, fname, lname, regdate, regplace, gender, f_fname, f_lname, m_fname, m_lname):
    insertions = (regno, fname, lname, regdate, regplace, gender, f_fname,f_lname, m_fname, m_lname)
    c.execute('INSERT INTO births VALUES(?,?,?,?,?,?,?,?,?,?);', insertions)

def create_marriage(regno, regdate, regplace, p1_fname, p1_lname, p2_fname, p2_lname):
    insertions = (regno, regdate, regplace, p1_fname, p2_lname, p2_fname, p2_lname)
    c.execute('INSERT INTO marriages VALUES(?,?,?,?,?,?,?);', insertions)

def create_payment(tno, pdate, amount):
    insertions = (tno, pdate, amount)
    c.execute("INSERT INTO payments VALUES(?,?,?)", insertions)

def create_ticket(tno, regno, fine, violation, vdate):
    insertions = (tno, regno, fine, violation, vdate)
    c.execute("INSERT INTO tickets VALUES(?,?,?,?,?)", insertions)

def get_city_of_user(uid):
    c.execute('''SELECT city, uid FROM users''')
    city = c.fetchall()
    for x in city:
        if(x[1].lower() == uid.lower()):
            return x[0]
