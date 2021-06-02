import requests

payload = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}
response = requests.post("https://reqres.in/api/register", data=payload)
print(response)
print(response.json()['token'])
