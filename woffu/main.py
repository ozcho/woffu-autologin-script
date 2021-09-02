import getpass
import json
from operator import itemgetter
import os.path
from . import woffu

def run():
    print("Woffu Autologin Script\n")
    saved_credentials = os.path.exists("./data.json")
    if (saved_credentials):
        with open("./data.json", "r") as json_data:
            login_info = json.load(json_data)
            domain, username, password, user_id, company_id = itemgetter(
                "domain",
                "username",
                "password",
                "user_id",
                "company_id"
            )(login_info)
    else:
        username = input("Enter your Woffu username:\n")
        password = getpass.getpass("Enter your password:\n")

    auth_headers = woffu.get_auth_headers(username, password)

    if (not saved_credentials):
        domain, user_id, company_id = woffu.get_domain_company_user_id(auth_headers)

    if (woffu.sign_in(domain, user_id, auth_headers)):
        print ("Success!")
    else:
        print ("Something went wrong when trying to log you in/out.")

    if (not saved_credentials):
        woffu.save_data(username, password, user_id, company_id, domain)