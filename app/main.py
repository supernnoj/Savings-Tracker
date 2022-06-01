from init_db import database
from tos import *
from login import *

def __init__():

    isOK_db = database.__init__()

    if isOK_db:
        print(f'\n GET TOS')
        isOK_tos = tos.__init__()

        if isOK_tos:
            print(f' TOS OK')
            print(f'\n GET LOGIN')
            login.__init__()

__init__()