from sys import exit
import requests


URL = "https://httpbin.org/encoding/utf8"
def make_request(url, timeout=5):
    try:
        response = requests.get(url)
    except requests.HTTPError:
        exit(1)
    except requests.ReadTimeout:
        exit(2)
    return response.text

print(make_request(URL))
