import mysql.connector
import json
import os
from datetime import date
import re
from datetime import datetime

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
                    Q__bank_acc = f"CREATE TABLE bank (id INT AUTO_INCREMENT PRIMARY KEY, {_bank_acc['email']} TEXT, {_bank_acc['cash_type']} TEXT, {_bank_acc['cash_bal']} DECIMAL(65, 2))"
                    Q.execute(Q__bank_acc)
                    print(" ADDED BANK ACCOUNT FIELDS")

                    _logs = x_table["logs"]
                    Q_logs = f"CREATE TABLE logs (id INT AUTO_INCREMENT PRIMARY KEY, {_logs['email']} TEXT, {_logs['cash_in']} DECIMAL(65, 2), {_logs['cash_out']} DECIMAL(65, 2), {_logs['cash_type']} TEXT, {_logs['cash_type_before_bal']} DECIMAL(65, 2), {_logs['cash_type_after_bal']} DECIMAL(65, 2), {_logs['total_funds_before']} DECIMAL(65, 2),{_logs['total_funds_after']} DECIMAL(65, 2), {_logs['date']} TEXT, {_logs['time']} TEXT, {_logs['note']} TEXT)"
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


class bank:
    def get(email):
        Q = _db.cursor()
        Q.execute(f"USE userdata")
        Q.execute(f"SELECT COUNT(id) FROM bank WHERE email = '{email}'")
        get_this = Q.fetchone()
        return get_this[0]

    def total(email):
        Q = _db.cursor()
        Q.execute(f"USE userdata")
        Q.execute(f"SELECT SUM(cash_bal) FROM bank WHERE email = '{email}'")
        get_this = Q.fetchone()
        return get_this[0]

    def id(email):
        Q = _db.cursor()
        Q.execute(f"USE userdata")
        Q.execute(f"SELECT id FROM bank WHERE email = '{email}'")
        get_this = Q.fetchall()
        return get_this

    def bal(id):

        temp = re.findall(r"\d+", str(id))
        res = list(map(int, temp))

        Q = _db.cursor()
        Q.execute(f"USE userdata")
        Q.execute(f"SELECT cash_bal FROM bank WHERE id = {int(res[0])}")
        get_this = Q.fetchone()
        return get_this[0]

    def type(id):

        temp = re.findall(r"\d+", str(id))
        res = list(map(int, temp))

        Q = _db.cursor()
        Q.execute(f"USE userdata")
        Q.execute(f"SELECT cash_type FROM bank WHERE id = {int(res[0])}")
        get_this = Q.fetchone()

        return get_this[0]

    def write(email, type, bal, total):
        Q = _db.cursor()
        Q.execute(f"USE userdata")
        Q.execute(
            f"INSERT INTO bank (email, cash_type, cash_bal) VALUES ('{email}', '{type}','{bal}')"
        )

        now = datetime.now()
        dt_date = now.strftime("%m/%d/%y")
        dt_time = now.strftime("%H:%M:%S")

        after = float(total) + float(bal)

        Q.execute(
            f"INSERT INTO logs (email, cash_in, cash_type_before_bal, cash_type_after_bal, cash_out, cash_type, date, time, total_funds_before, total_funds_after, note) VALUES ('{email}', '{bal}', '{bal}', '{bal}', '0', '{type}', '{dt_date}','{dt_time}', '{total}', '{after}', 'Registered a new account.')"
        )
        _db.commit()
        print(f"\n account registered")
        return True

    def delete(type, email, id, bal, total):
        Q = _db.cursor()
        Q.execute(f"USE userdata")
        Q.execute(f"DELETE FROM bank WHERE id = {id}")

        after = float(total) - float(bal)

        now = datetime.now()
        dt_date = now.strftime("%m/%d/%y")
        dt_time = now.strftime("%H:%M:%S")

        Q.execute(
            f"INSERT INTO logs (email, note, date, time, total_funds_before, total_funds_after, cash_type) VALUES ('{email}', 'Unbinded an account.', '{dt_date}', '{dt_time}', '{total}', '{after}', '{type}')"
        )
        _db.commit()
        return True


class dblogs:
    def get(email):
        Q = _db.cursor()
        Q.execute(f"USE userdata")
        Q.execute(f"SELECT COUNT(id) FROM logs WHERE email = '{email}'")
        get_this = Q.fetchone()
        return get_this[0]

    def id(email):
        Q = _db.cursor()
        Q.execute(f"USE userdata")
        Q.execute(f"SELECT id FROM logs WHERE email = '{email}'")
        get_this = Q.fetchall()
        return get_this

    def date(id):

        temp = re.findall(r"\d+", str(id))
        res = list(map(int, temp))

        Q = _db.cursor()
        Q.execute(f"USE userdata")
        Q.execute(f"SELECT date FROM logs WHERE id = {int(res[0])}")
        get_this = Q.fetchone()
        return get_this[0]

    def time(id):

        temp = re.findall(r"\d+", str(id))
        res = list(map(int, temp))

        Q = _db.cursor()
        Q.execute(f"USE userdata")
        Q.execute(f"SELECT time FROM logs WHERE id = {int(res[0])}")
        get_this = Q.fetchone()
        return get_this[0]

    def note(id):

        temp = re.findall(r"\d+", str(id))
        res = list(map(int, temp))

        Q = _db.cursor()
        Q.execute(f"USE userdata")
        Q.execute(f"SELECT note FROM logs WHERE id = {int(res[0])}")
        get_this = Q.fetchone()
        return get_this[0]

    def type(id):

        temp = re.findall(r"\d+", str(id))
        res = list(map(int, temp))

        Q = _db.cursor()
        Q.execute(f"USE userdata")
        Q.execute(f"SELECT cash_type FROM logs WHERE id = {int(res[0])}")
        get_this = Q.fetchone()
        return get_this[0]

    def before_bal(id):

        temp = re.findall(r"\d+", str(id))
        res = list(map(int, temp))

        Q = _db.cursor()
        Q.execute(f"USE userdata")
        Q.execute(f"SELECT cash_type_before_bal FROM logs WHERE id = {int(res[0])}")
        get_this = Q.fetchone()
        return get_this[0]

    def cash_in(id):

        temp = re.findall(r"\d+", str(id))
        res = list(map(int, temp))

        Q = _db.cursor()
        Q.execute(f"USE userdata")
        Q.execute(f"SELECT cash_in FROM logs WHERE id = {int(res[0])}")
        get_this = Q.fetchone()
        return get_this[0]

    def cash_out(id):

        temp = re.findall(r"\d+", str(id))
        res = list(map(int, temp))

        Q = _db.cursor()
        Q.execute(f"USE userdata")
        Q.execute(f"SELECT cash_out FROM logs WHERE id = {int(res[0])}")
        get_this = Q.fetchone()
        return get_this[0]

    def funds_before(id):

        temp = re.findall(r"\d+", str(id))
        res = list(map(int, temp))

        Q = _db.cursor()
        Q.execute(f"USE userdata")
        Q.execute(f"SELECT total_funds_before FROM logs WHERE id = {int(res[0])}")
        get_this = Q.fetchone()
        return get_this[0]

    def funds_after(id):

        temp = re.findall(r"\d+", str(id))
        res = list(map(int, temp))

        Q = _db.cursor()
        Q.execute(f"USE userdata")
        Q.execute(f"SELECT total_funds_after FROM logs WHERE id = {int(res[0])}")
        get_this = Q.fetchone()
        return get_this[0]


class transac:
    def make(email, type, bal, cash_before, total, note, cash_out):
        Q = _db.cursor()
        Q.execute(f"USE userdata")

        cash_after = float(cash_before) + float(bal) - float(cash_out)
        print (cash_before)
        print (bal)
        print (cash_out)
        print (cash_after)
        print(email)
        print(type)
        Q.execute(
            f"UPDATE bank SET cash_bal = '{cash_after}' WHERE email = '{email}' AND cash_type = '{type}'"
        )

        now = datetime.now()
        dt_date = now.strftime("%m/%d/%y")
        dt_time = now.strftime("%H:%M:%S")

        total_after = float(total) + float(bal) - float(cash_out)

        Q.execute(
            f"INSERT INTO logs (email, cash_in, cash_type_before_bal, cash_type_after_bal, cash_out, cash_type, date, time, total_funds_before, note, total_funds_after) VALUES ('{email}', '{bal}', '{cash_before}', '{cash_after}', '{cash_out}', '{type}', '{dt_date}','{dt_time}', '{total}', '{note}', '{total_after}')"
        )
        _db.commit()
        print(f"\n transaction successful")
        return True
