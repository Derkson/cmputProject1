import sqlite3
global conn, c
conn = sqlite3.connect('./miniproject1.db')
c = conn.cursor()
c.execute(' PRAGMA foreign_keys=ON ')


def login(username, password):
    c.execute('SELECT uid, pwd FROM users;')
    rows = c.fetchall()

    for tuple in rows:
        if(tuple[0].lower() == username.lower()):
            if(tuple[1] == password):
                return True
            return False
    return False




def main():
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
