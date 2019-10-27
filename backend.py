import sqlite3
global conn, c
conn = sqlite3.connect('./miniproject1.db')
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
    c.execute('SELECT uid, utype FROM users;')
    rows = c.fetchall()
    for tuple in rows:
        if(tuple[0].lower() == uid.lower()):
            if(tuple[1] == "o"):
                return True
    return False



#Register a birth
def register_birth(fname, lname, gender, bdate, bplace, f_fname, f_lname, m_fname, m_lname):
    #regdate is today's date
    #will have to create a new row in birth and in person
    #regplace is city of user
    #create a unique regno
    #address and phone number of babies are the same as mothers
    #if parent not in database, get info on parent, only first and last name are necessary
    pass

#first make a function to see if the person exists
def exists(fname, lname):
    c.execute('SELECT fname, lname FROM persons;')
    rows = c.fetchall()
    for tuple in rows:
        if(tuple[0].lower() == fname.lower() and tuple[1].lower() == lname.lower()):
            return True
    return False

#if the person doesn't exist, we must add them to the database
#might also be used for when the birth is registered
def create_person(fname, lname, bdate, bplace, address, phone):
    insertions = (fname, lname, bdate, bplace, address, phone)
    c.execute('INSERT INTO persons VALUES(?,?,?,?,?,?);',insertions)
    conn.commit()


def main():
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
