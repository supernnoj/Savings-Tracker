from database import *
from tos import *
from front import *
from user import *
from splash import *
from system import *
from new import *


def __init__():

    isOK_splash = splash.__init__()

    if isOK_splash:
        isOK_db = database.__init__()

        if isOK_db:
            print(f"\n GET TOS")
            isOK_tos = tos.__init__()

            if isOK_tos:
                print(f" TOS OK")
                print(f"\n GET HOME")
                isOK_login = app.__init__()

                if isOK_login:
                    print(f"\n GET USER SETTINGS")
                    print(f"\n user : {Q.get_user(Q.get_active())}")
                    print(f" new user : {Q.verify_new(Q.get_active())}")
                    if Q.verify_new(Q.get_active()):
                        if message.hello_user(Q.get_user(Q.get_active())):
                            if message.add_info():
                                if new_user.true():
                                    user.welcome()
                    else:
                        user.welcome()


__init__()
