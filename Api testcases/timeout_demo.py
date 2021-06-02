import requests

response = requests.get("https://httpbin.org/delay/5", timeout=3)
print(response.status_code)
