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
    find_car_owner("tank", "panzer iv", "1944", "green", "tank")
    find_car_owner("tank", "panzer iv", None, "green", "tank")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
