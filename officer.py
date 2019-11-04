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

def get_regno_info(regno):
    c.execute('''SELECT r.fname, r.lname, v.make, v.model, v.color
                 FROM registrations r, vehicles v
                 WHERE r.vin = v.vin
                 AND r.regno=:regno;''',
                 {"regno":regno})

    vehicleinfo = c.fetchone()
    return vehicleinfo

def issue_ticket(regno, violation, fine, vdate):
    #provide regno and get the name, make, model, year and color
    #provide vdate, violation, fine
    #create unique tno and ticket created
    tno = make_regno("tickets")
    #if no date is provided, vdate is today
    if(not vdate):
        vdate = date.today()

    create_ticket(tno, regno, fine, violation, vdate)

def find_car_owner(make, model, year, color, plate):
    #return all matches based on provided info, not everything needs to be entered
    #allow the user to select one
    #during the matches, display
        #make, model, year, color, regdate, expiry, fname, lname of neweset owner

    q = '''SELECT v.make, v.model, v.color, r.regdate, r.expiry, r.fname, r.lname
                 FROM registrations r, vehicles v
                 WHERE lower(v.make) LIKE '%{make}%'
                 AND lower(v.model) LIKE '%{model}%'
                 AND v.year LIKE '%{year}%'
                 AND lower(v.color) LIKE '%{color}%'
                 AND lower(r.plate) LIKE '%{plate}%';'''

    print(q.format(make = make.lower(), model = model.lower(), year = year, color = color.lower(), plate = plate.lower()))
    c.execute(q.format(make = make.lower(), model = model.lower(), year = year, color = color.lower(), plate = plate.lower()))
    rows = c.fetchall()
    print(rows)
