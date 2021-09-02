import requests
import json
from datetime import datetime

# aux functions
def get_auth_headers(username, password):
    # we need to get the Bearer access token for every request we make to Woffu
    print("Getting access token...\n")
    access_token = requests.post(
        "https://app.woffu.com/token",
        data = f"grant_type=password&username={username}&password={password}"
    ).json()['access_token']
    return {
        'Authorization': 'Bearer ' + access_token,
        'Accept': 'application/json',
        'Content-Type': 'application/json;charset=utf-8'
    }


def get_domain_company_user_id(auth_headers):
    # This function should only be called the first time the script runs.
    # We'll store the results for subsequent executions
    print("Getting IDs...\n")
    users = requests.get(
        "https://app.woffu.com/api/users", 
        headers = auth_headers
    ).json()
    company = requests.get(
        f"https://app.woffu.com/api/companies/{users['CompanyId']}", 
        headers = auth_headers
    ).json()
    return company['Domain'], users['UserId'], users['CompanyId']


def sign_in(domain, user_id, auth_headers):
    #Actually log in
    print("Sending sign request...\n")
    return requests.post(
        f"https://{domain}/api/svc/signs/signs",
        json = {
            'StartDate': datetime.now().replace(microsecond=0).isoformat()+"+01:00",
            'EndDate': datetime.now().replace(microsecond=0).isoformat()+"+01:00",
            'TimezoneOffset': "-60",
            'UserId': user_id
        },
        headers = auth_headers
    ).ok


def save_data(username, password, user_id, company_id, domain):
    #Store user/password/id to make less network requests in next logins
    with open("data.json", "w") as login_info:
        json.dump(
            {
                "username": username,
                "password": password,
                "user_id": user_id,
                "company_id": company_id,
                "domain": domain
            },
            login_info
        )


def get_holidays(domain, user_id, auth_headers):
    holidays = requests.get(
        f"https://{domain}/api/users/{user_id}/requests?pageSize=1000", 
        headers = auth_headers
    ).json()
    return holidays


def get_pending_holidays(domain, user_id, auth_headers):
    pending_holidays = [req for req in get_holidays(domain, user_id, auth_headers)
        if req['RequestStatusId'] == 20 and req['RequestStatus'] == '_RequestStatusAcceptedAndPending']
    return pending_holidays


def should_I_sign_in_today(domain, user_id, auth_headers):
    pending_holidays = get_pending_holidays(domain, user_id, auth_headers)
    today = datetime.today()
    should_i = any([(today >= datetime.datetime.fromisoformat(h['StartDate']).date() and today <= datetime.datetime.fromisoformat(h['EndDate']).date()) for h in pending_holidays])
    return should_i