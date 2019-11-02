import sqlite3
import random
from datetime import date
import create
global conn, c
path = './miniproject1.db'
conn = sqlite3.connect(path)
c = conn.cursor()
c.execute(' PRAGMA foreign_keys=ON ')


#determines if a person entered a valid username and password
def login(username, password):
    c.execute('SELECT uid, pwd FROM users;')
    rows = c.fetchall()
    for tuple in rows:
        if(tuple[0].lower() == username.lower()):
            if(tuple[1] == password):
                return 0 #vaild username and password
            return 1 #valid username, invalid password
    return 2 #invalid username


#determines if a person is an officer or not
def officer(uid):
    c.execute('SELECT uid FROM users WHERE utype = "o";')
    rows = c.fetchall()
    for (x,) in rows:
        if (uid.lower() == x.lower()):
            return True
    return False


#sees if a person is in the database
def persons_exists(fname, lname):
    c.execute('SELECT fname, lname FROM persons;')
    rows = c.fetchall()
    for tuple in rows:
        if(tuple[0].lower() == fname.lower() and tuple[1].lower() == lname.lower()):
            return True
    return False


def regno_exists(regno):
    c.execute('SELECT regno FROM registrations;')
    rows = c.fetchall()
    for tuple in rows:
        if(tuple[0] == regno):
            return True
    return False

def vin_exists(vin):
    c.execute("SELECT vin, FROM vehicles")
    rows = c.fetchall()
    for x in rows:
        if(x[0] == vin):
            return True
    return False
