from sqlite3 import connect
from webbrowser import get
import mysql.connector

dbconnect = mysql.connector.connect(host="localhost", user="root", password="")

class Q():

    def verify_user(user):
        Q = dbconnect.cursor()
        Q.execute(f'USE userdata')
        Q.execute(f"SELECT username FROM user_login WHERE email LIKE '%{user}'")
        get_this = Q.fetchone()
        if get_this:
            return True
        else:
            return False
    
    def  verify_pw(user, pw):
        Q = dbconnect.cursor()
        Q.execute(f'USE userdata')
        #print(f'query.py: {user}, {pw}') # just to check
        Q.execute(f"SELECT password FROM user_login WHERE username LIKE '%{user}'")
        get_this = Q.fetchone()
        if len(get_this) != 0:
            if get_this[0] == f'{pw}':
                return True
            else:
                return False
        else:
            return False
