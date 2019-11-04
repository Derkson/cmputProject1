import sqlite3
import random
import datetime
import sys
from create import *
from validation import *
global conn, c
path = sys.argv[1]
conn = sqlite3.connect(path)
c = conn.cursor()
c.execute(' PRAGMA foreign_keys=ON ')


#gets todays date
#checks if birthdate is valid
#gets a city for regplace
#creates a unique regno
#gets an address and phone number from mother
#adds a person to the tables
#adds a birth to the tables
def register_birth(fname, lname, gender, bdate, bplace, f_fname, f_lname, m_fname, m_lname, uid):
    #regdate is today's date
    regdate = datetime.date.today()
    #regplace is city of user
    city = get_city_of_user(uid)
    #create a unique regno
    regno = make_regno("births")

    m_fname = m_fname.lower()
    m_lname = m_lname.lower()
    #address and phone number of babies are the same as mothers
    c.execute('''SELECT DISTINCT phone, address
                 FROM persons
                 WHERE lower(fname) =:firstname
                 AND lower(lname) =:lastname;''',
                 {"firstname":m_fname, "lastname":m_lname})

    rows = c.fetchall()
    phone = rows[0]
    address = rows[1]

    create_person(fname, lname, bdate, bplace, address, phone)
    create_birth(regno, fname, lname, regdate, regplace, gender, f_fname, f_lname, m_fname, m_lname)
    return 1
#makes a regdate
#makes a unique regno
#gets a city for regplace
#uploads into table
def register_marriage(p1_fname, p1_lname, p2_fname, p2_lname, uid):
    regdate = datetime.date.today() #regdate is today
    regno = make_regno("marriages") #unique regno
    regplace = get_city_of_user(uid) #regplace is city of users
    create_marriage(regno, regdate, regplace, p1_fname, p1_lname, p2_fname, p2_lname)

#complete
def renew_vehicle(regno):
    #if registration expires today or is expired, new expiry is one year from today
    #else just add one year to the expiry date
    #'case when' in sql
    c.execute('''UPDATE registrations
                 SET expiry = CASE
                                 WHEN expiry <= date("now") THEN date("now", "+1 year")
                                 ELSE date(regdate, "+1 year")
                              END
                 WHERE regno=:regno;''',
                 {"regno":regno})
    conn.commit()

#finds regno
#if it is a valid regno, then set the expiry date on old registration
#create a new registration wit new owner etc.
def bill_of_sale(vin, o_fname, o_lname, new_fname, new_lname, newplate):
    #old registration has expiry of today
    #create a new registration
    newregno = make_regno("vehicles")
    vin = vin.lower()
    o_fname = o_fname.lower()
    o_lname = o_lname.lower()
    new_fname = new_fname.lower()
    new_lname = new_lname.lower()

    c.execute('''SELECT regno
                 FROM registrations
                 WHERE lower(vin)=:vin
                 AND lower(fname)=:o_fname
                 AND lower(lname)=:o_fname;''',
                 {"vin":vin, "o_fname":o_fname, "o_lname":o_lname})
    regno = c.fetchall()

    if(regno_exists(regno)):
        c.execute('''UPDATE registrations
                     SET expiry = date("now")
                     WHERE regno=:regno;''',
                     {"regno":regno})

        insertions = (newregno, newplate, vin, new_fname, new_lname)
        c.execute('''INSERT INTO registrations VALUES(?,date("now"),date("now", "+1 year"),?,?,?,?)''', insertions)
    else:
        return
    conn.commit()

#returns 1 if the input amount is negative
#returns 0 if you overpay
def process_payment(tno, amount):
    #can make multiple payments to pay off ticket, but sum cannot exceed total
    pdate = datetime.date.today()
    if amount < 0:
        return 0#cant have a negative poyment
    create_payment(tno, pdate, amount)

    c.execute('''SELECT fine
                 FROM tickets
                 WHERE tno=:tno;''',
                 {"tno":tno})

    row = c.fetchone()
    print("old amount owing: ", int(row[0]))

    newAmount = int(row[0]) - amount
    if(newAmount < 0):
        return 1

    c.execute('''UPDATE tickets
                 SET fine=:amountowe
                 WHERE tno=:tno;''',
                 {"amountowe":newAmount, "tno":tno})
    return 2
'''
Order of info in list
tuple of number of tickets, lifetime
tuple of number of demerit notices and sum of points, lifetime
tuple of number of tickets, past 2 years
tuple of number of demerit notices and sum of points, past 2 years
tickets with info
    tno, vdate, violation, fine amount, make of car, model of car
'''
def driver_abstract(fname, lname):
    #get number of ticekts, demerit points, demerit notices
    #all within two years or lifetime

    #ticket number lifetime
    fname = fname.lower()
    lname = lname.lower()
    c.execute('''SELECT count(t.tno)
                 FROM tickets t, persons p, registrations r
                 WHERE t.regno = r.regno
                 AND lower(r.fname)=:firstname
                 AND lower(r.lname)=:lastname
                 AND lower(r.fname) = lower(p.fname)
                 AND lower(r.lname) = lower(p.lname);''',
                {"firstname":fname, "lastname":lname})

    ticketnum_life = c.fetchall()
    c.execute('''SELECT count(*), sum(d.points)
                 FROM demeritNotices d, persons p
                 WHERE lower(d.fname) = lower(p.fname)
                 AND lower(d.lname) = lower(p.lname)
                 AND lower(p.fname)=:firstname
                 AND lower(p.lname)=:lastname;''',
                 {"firstname":fname, "lastname":lname})
    demeritinfo_life = c.fetchall()

    c.execute('''SELECT count(t.tno)
                 FROM tickets t, persons p, registrations r
                 WHERE t.regno = r.regno
                 AND lower(r.fname)=:firstname
                 AND lower(r.lname)=:lastname
                 AND lower(r.fname) = lower(p.fname)
                 AND lower(r.lname) = lower(p.lname)
                 AND t.vdate > date("now", "-2 years");''',
                {"firstname":fname, "lastname":lname})

    ticketnum_2years = c.fetchall()
    c.execute('''SELECT count(*), sum(d.points)
                 FROM demeritNotices d, persons p
                 WHERE lower(d.fname) = lower(p.fname)
                 AND lower(d.lname) = lower(p.lname)
                 AND lower(p.fname)=:firstname
                 AND lower(p.lname)=:lastname
                 AND d.ddate > date("now", "-2 years");''',
                 {"firstname":fname, "lastname":lname})
    demeritinfo_2years = c.fetchall()

    #given ticket info, can order asc or desc by date
    c.execute('''SELECT DISTINCT t.tno, t.vdate, t.violation, t.fine, v.make, v.model
                 FROM tickets t, vehicles v, registrations r, persons p
                 WHERE t.regno = r.regno
                 AND lower(r.vin) = lower(v.vin)
                 AND lower(p.fname)=:firstname
                 AND lower(p.lname)=:lastname
                 AND lower(r.fname) = lower(p.fname)
                 AND lower(r.lname) = lower(p.lname)
                 ORDER BY t.vdate asc;''',
                 {"firstname":fname, "lastname":lname})
    ticketinfo = c.fetchall()
    joinedlist = ticketnum_life + demeritinfo_life + ticketnum_2years + demeritinfo_2years + ticketinfo

    #view no more than 5 at a time
    return joinedlist
