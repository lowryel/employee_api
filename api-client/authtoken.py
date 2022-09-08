#Token Authentication

from getpass import getpass
import requests
username=input("Your username\n")
password=getpass("Your password\n")
auth_url = "http://localhost:8000/authtoken/"
auth_response = requests.post(auth_url, json={'username':username, 'password':password})
details = auth_response.json()
print(details)
if auth_response.status_code==200:
    token=auth_response.json()['token']
    print(token)
    headers={"Authorization": f"Token {token}"}
    print(headers)
    url = "http://localhost:8000/emplist_create/"
    response=requests.get(url, headers=headers)
    details=response.json()
    print(details)
