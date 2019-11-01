import sqlite3
import random
import datetime
import create
import validation
global conn, c
path = './miniproject1.db'
conn = sqlite3.connect(path)
c = conn.cursor()
c.execute(' PRAGMA foreign_keys=ON ')

#generates a random registration number


#Register a birth, complete???
def register_birth(fname, lname, gender, bdate, bplace, f_fname, f_lname, m_fname, m_lname, uid):
    #regdate is today's date
    regdate = datetime.datetime.now()
    #regplace is city of user, need to figure out who our user is
    city = get_city_of_user(uid)
    #create a unique regno
    regno = make_regno("births")

    #address and phone number of babies are the same as mothers
    c.execute('''SELECT DISTINCT phone, address
                 FROM persons
                 WHERE fname =:firstname
                 AND lname =: lastname;''',
                 {"firstname":fname, "lastname":lname})

    rows = c.fetchall()
    phone = rows[0]
    address = rows[1]

    create_person(fname, lname, bdate, bplace, address, phone)
    create_birth(regno, fname, lname, regdate, regplace, gender, f_fname, f_lname, m_fname, m_lname)
    conn.commit()

#register a marriage, complete???
def register_marriage(p1_fname, p1_lname, p2_fname, p2_lname, uid):
    regdate = datetime.datetime.now() #regdate is today
    regno = make_regno("marriages") #unique regno
    city = get_city_of_user(uid) #regplace is city of users
    create_marriage(regno, regdate, regplace, p1_fname, p1_lname, p2_fname, p2_lname)
    conn.commit()


def renew_vehicle(regno):
    pass

def main():
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
