import json

import requests

# with open('../ApiPractice/APIcontract/create_user.json') as file:
# data = json.load(f)
# print(data)

data = open("../ApiPractice/APIcontract/create_user.json", "r").read()

response = requests.post("https://reqres.in/api/users", data=json.loads(data))
print(response)
print(response.json())
print(response.headers.get("Content-Type"))
assert response.json()['job'] == 'SDET'
