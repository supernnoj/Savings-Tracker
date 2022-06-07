import mysql.connector
import json
import os
from datetime import date

# ========= >>> connect to xampp/local server <<< =========
_db = mysql.connector.connect(host="localhost", user="root", password="")


class database:
    def __init__():
        print("\n START CONNECT\n")
        Q = _db.cursor()
        print(" GET SERVER")
        print(" RUN SERVER\n")
        print(" SERVER RUNNING ...\n")

        # Q.execute("drop database userdata") # to drop database : only use if necessary

        db_exists = False
        print(" GET DATABASE")
        Q.execute("SHOW DATABASES")

        for exist_db in Q:
            if str(exist_db) == "('userdata',)":
                print(" FOUND DATABASE")
                Q.execute("USE userdata")
                Q.execute("truncate table active")
                # _db.commit()
                db_exists = True
        if db_exists == False:
            print("\n ERROR: NO INITIAL DATABASE FOUND\n")
            print(" SYTEM WILL NOW IMPLEMENT CREATION OF DATABASE\n")
            print(" CREATING NEW DATABASE")
            Q.execute("CREATE DATABASE IF NOT EXISTS userdata")
            Q.execute("USE userdata")
            to_file = os.getcwd() + "\\app\\"
            print(" LOCATING DATABASE CONFIGURATIONS")
            Q_active = (
                f"CREATE TABLE active (id INT AUTO_INCREMENT PRIMARY KEY, email TEXT)"
            )
            Q.execute(Q_active)
            Q_setup = f"CREATE TABLE setup (id INT AUTO_INCREMENT PRIMARY KEY, email TEXT,  status TEXT)"
            Q.execute(Q_setup)
            Q_security = f"CREATE TABLE security (id INT AUTO_INCREMENT PRIMARY KEY, email TEXT,  question TEXT, answer TEXT)"
            Q.execute(Q_security)

            with open(to_file + "database.json", "r") as open_tables:
                print(" APPLYING DATABASE CONFIGURATIONS\n")
                get_table = json.load(open_tables)

                for x_table in get_table:
                    _user_login = x_table["user_login"]
                    Q_user_login = f"CREATE TABLE user (id INT AUTO_INCREMENT PRIMARY KEY, {_user_login['username']} TEXT, {_user_login['password']} TEXT, {_user_login['email']} TEXT)"
                    Q.execute(Q_user_login)
                    print(" ADDED USER LOGIN FIELDS")

                    _user_profile = x_table["user_profile"]
                    Q_user_profile = f"CREATE TABLE profile (id INT AUTO_INCREMENT PRIMARY KEY, email TEXT, {_user_profile['fname']} TEXT, {_user_profile['mi']} TEXT, {_user_profile['lname']} TEXT, {_user_profile['age']} INT, {_user_profile['birthday']} TEXT)"
                    Q.execute(Q_user_profile)
                    print(" ADDED USER PROFILE FIELDS")

                    _bank_acc = x_table["bank_acc"]
                    Q__bank_acc = f"CREATE TABLE bank (id INT AUTO_INCREMENT PRIMARY KEY, {_bank_acc['email']} TEXT, {_bank_acc['cash_type']} TEXT, {_bank_acc['cash_bal']} NUMERIC)"
                    Q.execute(Q__bank_acc)
                    print(" ADDED BANK ACCOUNT FIELDS")

                    _logs = x_table["logs"]
                    Q_logs = f"CREATE TABLE logs (id INT AUTO_INCREMENT PRIMARY KEY, {_logs['email']} TEXT, {_logs['cash_in']} NUMERIC, {_logs['cash_out']} NUMERIC, {_logs['cash_type']} TEXT, {_logs['cash_type_before_bal']} NUMERIC, {_logs['cash_type_after_bal']} NUMERIC, {_logs['total_funds_before']} NUMERIC,{_logs['total_funds_after']} NUMERIC, {_logs['date']} TEXT, {_logs['time']} TEXT, {_logs['note']} TEXT)"
                    Q.execute(Q_logs)
                    print(" ADDED LOGS FIELDS")

            print("\n DATABASE CREATED")

        print("\n START APP")
        return True


class Q:
    def verify_user(user):
        Q = _db.cursor()
        Q.execute(f"USE userdata")
        Q.execute(f"SELECT username FROM user WHERE username LIKE '%{user}'")
        get_this = Q.fetchone()
        if get_this:
            return True
        else:
            return False

    def verify_pw(user, pw):
        Q = _db.cursor()
        Q.execute(f"USE userdata")
        Q.execute(f"SELECT password FROM user WHERE username LIKE '%{user}'")
        get_this = Q.fetchone()
        if len(get_this) != 0:
            if get_this[0] == f"{pw}":
                return True
            else:
                return False
        else:
            return False

    def verify_email(email):
        Q = _db.cursor()
        Q.execute(f"USE userdata")
        Q.execute(f"SELECT email FROM user WHERE email LIKE '%{email}'")
        get_this = Q.fetchone()
        if get_this:
            return True
        else:
            return False

    def verify_new(email):
        Q = _db.cursor()
        Q.execute(f"USE userdata")
        Q.execute(f"SELECT status FROM setup WHERE email LIKE '%{email}'")
        get_this = Q.fetchone()
        if get_this[0] == f"new":
            return True
        else:
            return False

    def get_email(user):
        Q = _db.cursor()
        Q.execute(f"USE userdata")
        Q.execute(f"SELECT email FROM user WHERE username LIKE '%{user}'")
        get_this = Q.fetchone()
        return get_this[0]

    def get_user(email):
        Q = _db.cursor()
        Q.execute(f"USE userdata")
        Q.execute(f"SELECT username FROM user WHERE email LIKE '%{email}'")
        get_this = Q.fetchone()
        return get_this[0]

    def create_user(email, user, pw):
        Q = _db.cursor()
        Q.execute(f"USE userdata")
        Q.execute(
            f"INSERT INTO user (email, username, password) VALUES ('{email}', '{user}', '{pw}')"
        )
        Q.execute(f"INSERT INTO setup (email, status) VALUES ('{email}', 'new')")
        _db.commit()
        print(f"\n USER ADDED")
        return True

    def get_active():
        Q = _db.cursor()
        Q.execute(f"USE userdata")
        Q.execute(f"SELECT email FROM active WHERE id LIKE '%1'")
        get_this = Q.fetchone()
        return get_this[0]

    def set_active(email):
        Q = _db.cursor()
        Q.execute(f"USE userdata")
        Q.execute(f"INSERT INTO active (email) VALUES ('{email}')")
        _db.commit()
        print(f"\n SET ACTIVE")
        return True

    def write_profile(email, fname, mi, lname, birthday, sq, sa):
        Q = _db.cursor()
        dob = birthday.split("-")
        year = dob[2]
        current_year = date.today().year
        age = (int(year) - int(current_year)) * (-1)
        print(year)
        print(age)
        Q.execute(f"USE userdata")
        Q.execute(
            f"INSERT INTO profile (email, fname, mi, lname, age, birthday) VALUES ('{email}', '{fname}','{mi}','{lname}', '{int(age)}','{birthday}')"
        )
        Q.execute(f"UPDATE setup SET status = 'old' WHERE email = '{email}' ")
        Q.execute(
            f"INSERT INTO security (email, question, answer) VALUES ('{email}', '{sq}', '{sa}')"
        )
        _db.commit()
        print(f"\n user info added")
        return True
