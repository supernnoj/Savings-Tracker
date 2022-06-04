from database import *
from tos import *
from front import *
from user import *
from splash import *

def __init__():

    isOK_splash = True # work in progress

    if isOK_splash:
        isOK_db = database.__init__()

        if isOK_db:
            print(f'\n GET TOS')
            isOK_tos = tos.__init__()

            if isOK_tos:
                print(f' TOS OK')
                print(f'\n GET HOME')
                isOK_login = app.__init__()

                if isOK_login:
                    print(f'\n GET USER APP')
                    isOK_user = user.welcomepage()
                
__init__()