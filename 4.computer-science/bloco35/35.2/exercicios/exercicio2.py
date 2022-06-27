import requests
import json


def get_users():
    URL = "https://api.github.com/users"
    user_list = []
    try:
        response = requests.get(URL)
    except requests.HTTPError:
        exit(1)
    except requests.ReadTimeout:
        exit(2)
    users = json.loads(response.text)
    for user in users:
        print(f'{user["login"]} {user["url"]}')

get_users()
