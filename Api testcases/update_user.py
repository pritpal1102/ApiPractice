import json
import requests

payload = {
    "name": "shanky",
    "job": "API"
}

response = requests.put("https://reqres.in/api/users/2", data=payload)
print(response)
print(response.json())
assert (response.json()['job']) == 'API'
