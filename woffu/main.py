import getpass
import json
from operator import itemgetter
import os
from .woffu import Woffu

def run():
    print("Woffu Autologin Script\n")
    
    username=os.getenv('WOFFU_USER')
    password=os.getenv('WOFFU_PASS')

    client = Woffu(username, password)

    if (client.sign_in()):
        print ("Success!")
    else:
        print ("Something went wrong when trying to log you in/out.")
