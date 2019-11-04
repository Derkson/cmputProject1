import sqlite3
import sys
global conn, c
path = sys.argv[1]
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

#sees if a regno is in the database
def regno_exists(regno):
    c.execute('SELECT regno FROM registrations;')
    rows = c.fetchall()
    for tuple in rows:
        if(tuple[0] == regno):
            return True
    return False

#sees if a vin is in the database
def vin_exists(vin):
    c.execute("SELECT lower(vin) FROM vehicles")
    rows = c.fetchall()
    for x in rows:
        if(x[0].lower() == vin):
            return True
    return False

#taking in a fname, lname and vin
#determines if they have owned a specific car and if they
#are the current owner 
def is_current_owner(fname, lname, vin):
    fname = fname.lower()
    lname = lname.lower()
    vin = vin.lower()
    c.execute('''SELECT fname, lname, vin, regdate
                 FROM registrations
                 WHERE lower(fname)=:fname
                 AND lower(lname)=:lname
                 AND lower(vin)=:vin
                 ORDER BY regdate desc;''',
                 {"fname":fname, "lname":lname, "vin":vin})
    info = c.fetchone()
    print(info)

    if(not info):
        return False
    if(info[0].lower() == fname and info[1].lower() == lname and info[2].lower() == vin):
        return True
    return False
