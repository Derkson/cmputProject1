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
    if(make is not None):
        make = make.lower()
    if(model is not None):
        model = model.lower()
    if(color is not None):
        color = color.lower()
    if(plate is not None):
        plate = plate.lower()

    c.execute('''SELECT v.make, v.model, v.year, v.color, r.regdate, r.expiry, r.fname, r.lname
                 FROM vehicles v, registrations r
                 WHERE r.vin = v.vin
                 AND
                 (
                    CASE WHEN model NOT NULL THEN lower(v.model)=:model
                    CASE WHEN make NOT NULL THEN lower(v.make)=:make
                    CASE WHEN year NOT NULL THEN lower(v.year)=:year
                    CASE WHEN color NOT NULL THEN lower(v.color)=:color 
                    CASE WHEN plate NOT NULL THEN lower(r.plate)=:plate END)
                ;''',
                 {"make":make, "model":model, "year":year, "color":color, "plate":plate})
    info = c.fetchall()
    print(info)
