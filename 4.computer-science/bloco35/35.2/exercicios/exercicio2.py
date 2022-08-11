import requests
import json


def get_users(timeout=5):
    URL = "https://api.github.com/users"
    try:
        response = requests.get(URL, timeout=timeout)
    except requests.HTTPError:
        exit(1)
    except requests.ReadTimeout:
        exit(2)
    users = json.loads(response.text)
    for user in users:
        print(f'{user["login"]} {user["url"]}')


get_users()
