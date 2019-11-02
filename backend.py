import sqlite3
import random
from datetime import date, timedelta
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
<<<<<<< HEAD
    print(get_city_of_user("U007"))
    #driver_abstract("Chris", "Pontikes", False, False)
    #driver_abstract("Josh", "Derkson", False, False)
    #driver_abstract("Alex", "Rostron", True, True)
=======
>>>>>>> develop
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
