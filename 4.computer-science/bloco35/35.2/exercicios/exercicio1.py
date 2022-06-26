import requests


URL = "https://httpbin.org/encoding/utf8"
def make_request(url):
    response = requests.get(url)
    return response.text

print(make_request(URL))
