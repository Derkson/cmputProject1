import sqlite3
import random
import UI
import sys
global conn, c
path = sys.argv[1]
conn = sqlite3.connect(path)
c = conn.cursor()
c.execute(' PRAGMA foreign_keys=ON ')

#creates a unique regno dependent on what table you need it for
def make_regno(table):
    regno = random.randint(1,1000)
    #which table do you need the table for, gets all regno from that table
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
    #compares them all to see if it's unique, if not, recursively call the function
    for (x,) in rows:
        if(x == regno):
            return make_regno(table)
    conn.commit()
    return regno


#all functions with 'create' simply take an imput and insert the values into the table
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

def create_payment(tno, pdate, amount):
    insertions = (tno, pdate, amount)
    c.execute("INSERT INTO payments VALUES(?,?,?);", insertions)
    conn.commit()

def create_ticket(tno, regno, fine, violation, vdate):
    insertions = (tno, regno, fine, violation, vdate)
    c.execute("INSERT INTO tickets VALUES(?,?,?,?,?);", insertions)
    conn.commit()

#takes in the uid and finds the city
def get_city_of_user(uid):
    c.execute('''SELECT city, uid FROM users;''')
    city = c.fetchall()
    for x in city:
        if(x[1].lower() == uid.lower()):
            return str(x[0])
