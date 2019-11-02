import sqlite3
import random
from datetime import date, timedelta
from create import *
from validation import *
global conn, c
path = './miniproject1.db'
conn = sqlite3.connect(path)
c = conn.cursor()
c.execute(' PRAGMA foreign_keys=ON ')

#Register a birth, complete
def register_birth(fname, lname, gender, bdate, bplace, f_fname, f_lname, m_fname, m_lname, uid):
    #regdate is today's date
    regdate = date.today()
    #regplace is city of user
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

#register a marriage, complete
def register_marriage(p1_fname, p1_lname, p2_fname, p2_lname, uid):
    regdate = date.today() #regdate is today
    regno = make_regno("marriages") #unique regno
    city = get_city_of_user(uid) #regplace is city of users
    create_marriage(regno, regdate, regplace, p1_fname, p1_lname, p2_fname, p2_lname)
    conn.commit()

#complete, not pretty, can make prettier later
def renew_vehicle(regno):
    #if registration expires today or is expired, new expiry is one year from today
    #else just add one year to the expiry date
    #'case when' in sql
    c.execute('''SELECT *
                 FROM registrations
                 WHERE regno=:registrationNumber;''',
                 {"registrationNumber":regno})

    rows = c.fetchone()
    expdate = rows[2]
    year = int(expdate[0:4])
    month = int(expdate[5:7])
    day = int(expdate[8:10])

    if(date(year, month, day) > date.today()):
        newexp = date(year +1, month, day)
    else:
        newexp = date.today() + timedelta(days = 365)

    c.execute('''UPDATE registrations
                 SET expiry=:newexpiry
                 WHERE expiry=:expdate
                 AND regno=:registrationsNumber;''',
                 {"newexpiry":newexp, "expdate":expdate, "registrationsNumber":regno})
    conn.commit()

#pretty well works i guess
def bill_of_sale(vin, o_fname, o_lname, new_fname, new_lname, newplate):
    if(persons_exists(new_fname, new_lname) == False):
        print("well shit, cant sell to someone that dont exist")
        return
    elif(persons_exists(o_fname, o_lname) == False):
        print("That owner doesnt even exist bro")
        return

    c.execute('''SELECT fname, lname
                 FROM registrations
                 WHERE fname=:o_fname
                 AND lname=:o_lname
                 AND vin=:vin;''',
                 {"vin":vin,"o_fname":o_fname, "o_lname":o_lname})
    rows = c.fetchone()
    if(not rows):
        print("Error in vin")
        return

    print(rows[0], rows[1])
    c.execute('''DELETE FROM registrations
                 WHERE vin=:vin''',
                 {"vin":vin})

    newregno = make_regno("vehicles")
    newregdate = date.today()
    newexpdate = date.today() + timedelta(days = 365)
    create_registration(newregno, newregdate, newexpdate, newplate, vin, new_fname, new_lname)

#have a solution here, may need to change it
def process_payment(tno, amount):
    #can make multiple payments to pay off ticket, but sum cannot exceed total
    pdate = date.today()
    create_payment(tno, pdate, amount)

    c.execute('''SELECT fine
                 FROM tickets
                 WHERE tno=:tno;''',
                 {"tno":tno})

    row = c.fetchone()
    print("old amount owing: ", int(row[0]))

    newAmount = int(row[0]) - amount
    if(newAmount < 0):
        print("paid too much money")
        return
    elif(newAmount == 0):
        print("all paid up")
    print("new amount owing: ", newAmount)

    c.execute('''UPDATE tickets
                 SET fine=:amountowe
                 WHERE tno=:tno;''',
                 {"amountowe":newAmount, "tno":tno})


def driver_abstract(fname, lname):
    #get number of ticekts
    #number of demerit notices
    #total number of demerit points, within two years and lifetime
    #tickets can be ordered ascending or descending by date
    #each ticket will display tno, vdate, desc, fine, regno, make of car, model of car 

    pass

def main():
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
