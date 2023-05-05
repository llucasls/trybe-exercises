from requests import request


URL = "https://scrapethissite.com/pages/advanced/?gotcha=headers"

response = request("GET", URL, headers={"Accept": "text/html",
                                        "User-Agent": "chrome"})

print(response.text)
