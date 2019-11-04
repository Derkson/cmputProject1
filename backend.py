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
    '''
    print(persons_exists("josh", "derkson"))
    print(persons_exists("chris", "pontikes"))
    print(vin_exists("u003"))

    bill_of_sale("u003", "josh", "derkson", "chris", "pontikes", "mine")
    '''
    print(driver_abstract("chris", "pontikes"))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
