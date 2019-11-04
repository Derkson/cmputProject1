import sqlite3
import random
import sys
from create import *
from validation import *
from agent import *
from officer import *
global conn, c
path = sys.argv[1]
conn = sqlite3.connect(path)
c = conn.cursor()
c.execute(' PRAGMA foreign_keys=ON ')


def main():
    find_car_owner( "", "panzer iv", "1944", "green", "tank") #works
    find_car_owner("tank", "panzer iv", "", "green", "tank") #works
    find_car_owner("ford", "", "", "", "") #works
    find_car_owner("", "f150", "", "", "") #no work
    find_car_owner("", "", "2015", "", "")
    find_car_owner("", "", "", "red", "")
    find_car_owner("", "", "", "", "legoboi")
    find_car_owner("", "f150", "2015", "red", "legoboi")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
