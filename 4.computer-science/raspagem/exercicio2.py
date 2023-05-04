import json

from requests import request


URL = "https://api.github.com/users"

response = request("GET", URL)

users = json.loads(response.text)
for user in users:
    username = user["login"]
    url = user["url"]

    print(username, url)
