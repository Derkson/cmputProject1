import sqlite3
import random
import datetime
from create import *
from validation import *
global conn, c
path = './miniproject1.db'
conn = sqlite3.connect(path)
c = conn.cursor()
c.execute(' PRAGMA foreign_keys=ON ')


#Register a birth, complete, can make prettier
def register_birth(fname, lname, gender, bdate, bplace, f_fname, f_lname, m_fname, m_lname, uid):
    #regdate is today's date
    regdate = date.today()
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
                 AND lower(lname) =: lastname;''',
                 {"firstname":m_fname, "lastname":m_lname})

    rows = c.fetchall()
    phone = rows[0]
    address = rows[1]

    create_person(fname, lname, bdate, bplace, address, phone)
    create_birth(regno, fname, lname, regdate, regplace, gender, f_fname, f_lname, m_fname, m_lname)

#register a marriage, complete, can make prettier
def register_marriage(p1_fname, p1_lname, p2_fname, p2_lname, uid):
    regdate = date.today() #regdate is today
    regno = make_regno("marriages") #unique regno
    city = get_city_of_user(uid) #regplace is city of users
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

#complete
def bill_of_sale(vin, o_fname, o_lname, new_fname, new_lname, newplate):
    newregno = make_regno("vehicles")
    vin = vin.lower()
    o_fname=o_fname.lower()
    o_lname=o_lname.lower()
    c.execute('''DELETE FROM registrations
                 WHERE lower(vin)=:vin''',
                 {"vin":vin})

    c.execute('''UPDATE registrations
                 SET fname=:new_fname, lname=:new_lname, regno=:newregno, regdate = date("now"), expiry = date("now", "+1 year")
                 WHERE (lower(fname)=:o_fname AND lower(lname)=:o_lname);''',
                 {"new_fname":new_fname, "new_lname":new_lname, "newregno":newregno, "o_fname":o_fname, "o_lname":o_lname})

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
    c.execute('''SELECT count(t.tno)
                 FROM tickets t, persons p, registrations r
                 WHERE t.regno = r.regno
                 AND lower(r.fname)=:lower(firstname)
                 AND lower(r.lname)=:lower(lastname)
                 AND lower(r.fname) = lower(p.fname)
                 AND lower(r.lname) = lower(p.lname);''',
                {"firstname":fname, "lastname":lname})

    ticketnum_life = c.fetchall()
    c.execute('''SELECT count(*), sum(d.points)
                 FROM demeritNotices d, persons p
                 WHERE lower(d.fname) = lower(p.fname)
                 AND lower(d.lname) = lower(p.lname)
                 AND lower(p.fname)=:lower(firstname)
                 AND lower(p.lname)=:lower(lastname);''',
                 {"firstname":fname, "lastname":lname})
    demeritinfo_life = c.fetchall()

    c.execute('''SELECT count(t.tno)
                 FROM tickets t, persons p, registrations r
                 WHERE t.regno = r.regno
                 AND lower(r.fname)=:lower(firstname)
                 AND lower(r.lname)=:lower(lastname)
                 AND lower(r.fname) = lower(p.fname)
                 AND lower(r.lname) = lower(p.lname)
                 AND t.vdate > date("now", "-2 years");''',
                {"firstname":fname, "lastname":lname})

    ticketnum_2years = c.fetchall()
    c.execute('''SELECT count(*), sum(d.points)
                 FROM demeritNotices d, persons p
                 WHERE lower(d.fname) = lower(p.fname)
                 AND lower(d.lname) = lower(p.lname)
                 AND lower(p.fname)=:lower(firstname)
                 AND lower(p.lname)=:lower(lastname)
                 AND d.ddate > date("now", "-2 years");''',
                 {"firstname":fname, "lastname":lname})
    demeritinfo_2years = c.fetchall()

    #given ticket info, can order asc or desc by date
    c.execute('''SELECT t.tno, t.vdate, t.violation, t.fine, v.make, v.model
                 FROM tickets t, vehicles v, registrations r, persons p
                 WHERE t.regno = r.regno
                 AND r.vin = v.vin
                 AND lower(p.fname)=:lower(firstname)
                 AND lower(p.lname)=:lower(lastname)
                 AND lower(r.fname) = lower(p.fname)
                 AND lower(r.lname) = lower(p.lname)
                 ORDER BY t.vdate asc;''',
                 {"firstname":fname, "lastname":lname})
    ticketinfo = c.fetchall()
    joinedlist = ticketnum_life + demeritinfo_life + ticketnum_2years + demeritinfo_2years + ticketinfo

    #view no more than 5 at a time
    return joinedlist
