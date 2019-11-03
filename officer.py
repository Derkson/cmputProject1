import sqlite3
import random
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

    #create unique tno and ticket created
    tno = make_regno("tickets")
    #if no date is provided, vdate is today
    if(not vdate):
        vdate = date.today()

    create_ticket(tno, regno, fine, violation, vdate)
    return vehicleinfo

def find_car_owner(make, model, year, color, plate):
    #return all matches based on provided info, not everything needs to be entered
    #allow the user to select one
    #during the matches, display
        #make, model, year, color, regdate, expiry, fname, lname of neweset owner
