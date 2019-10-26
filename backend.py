import sqlite3
global conn, c
conn = sqlite3.connect('./miniproject1.db')
c = conn.cursor()
c.execute(' PRAGMA foreign_keys=ON ')


#determines if a person entered a valid username and password
def login(username, password):
    c.execute('SELECT uid, pwd FROM users;')
    rows = c.fetchall()

    for tuple in rows:
        if(tuple[0].lower() == username.lower()):
            if(tuple[1] == password):
                return 0 #vaild username and password
            return 1 #valid username, invalid password
    return 2 #invalid username


#determines if a person is an officer or not
def officer(uid):
    c.execute('SELECT uid, utype FROM users;')
    rows = c.fetchall()
    for tuple in rows:
        if(tuple[0].lower() == uid.lower()):
            if(tuple[1] == "o"):
                return True
    return False



#Register a birth

def main():
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
