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


def issue_ticket(regno, violation, fine, vdate):
    #provide regno and get the name, make, model, year and color
    #provide vdate, violation, fine
    c.execute('''SELECT r.fname, r.lname, v.make, v.model, v.color
                 FROM registrations r, vehicles v
                 WHERE r.vin = v.vin
                 AND r.regno=:regno;''',
                 {"regno":regno})

    vehicleinfo = c.fetchone()
    print(vehicleinfo)

    #create unique tno and ticket created
    tno = make_regno("tickets")
    #if no date is provided, vdate is today
    if(not vdate):
        vdate = date.today()

    create_ticket(tno, regno, fine, violation, vdate)

def find_car_owner(make, model, year, color, plate):
    pass
