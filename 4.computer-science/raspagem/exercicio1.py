from requests import request


URL = "https://httpbin.org/encoding/utf8"

response = request("GET", URL)

print(response.text)
