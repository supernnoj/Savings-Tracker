from init_db import Q
from tos import *
from home import *
from appuser import *

def __init__():

    isOK_db = Q.__init__()

    if isOK_db:
        print(f'\n GET TOS')
        isOK_tos = tos.__init__()

        if isOK_tos:
            print(f' TOS OK')
            print(f'\n GET HOME')
            isOK_login = home.__init__(f'', f'')

            if isOK_login:
                print(f'\n GET USER APP')
                isOK_user = app.welcomepage()
                
__init__()