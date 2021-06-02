import requests

response = requests.get("https://reqres.in/api/users?page=2")
statuscode = response.status_code
print(response)
print(type(response))
# assert statuscode == 201, "code doesnt match"

# print(response.text)

# print(response.content)

print(response.json())
print(response.headers)
print(response.cookies)
print(response.encoding)
print(response.url)


