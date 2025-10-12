import requests

LOGIN_URL = "https://erpx.gpgit.com/erp/academic/users/login"

USERNAME="TCS22054"

payload = {
    'user_field_name': USERNAME,
    'pass_field_name': USERNAME
    }
with requests.Session() as s:
    login_response = s.post(LOGIN_URL, data=payload)
    print(login_response)