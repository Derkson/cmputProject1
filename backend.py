import sqlite3
import random
from create import *
from validation import *
from agent import *
from officer import *
global conn, c
path = './miniproject1.db'
conn = sqlite3.connect(path)
c = conn.cursor()
c.execute(' PRAGMA foreign_keys=ON ')


def main():
    find_car_owner(None, "panzer iv", "1944", "green", "tank") #works
    find_car_owner("tank", "panzer iv", None, "green", "tank") #works
    find_car_owner("ford", None, None, None, None) #works
    find_car_owner(None, "f150", None, None, None) #no work
    find_car_owner(None, None, "2015", None, None)
    find_car_owner(None, None, None, "red", None)
    find_car_owner(None, None, None, None, "legoboi")
    find_car_owner(None, "f150", "2015", "red", "legoboi")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
