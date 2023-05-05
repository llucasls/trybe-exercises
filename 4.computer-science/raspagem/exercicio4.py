from requests import request
from parsel import Selector


URL = "http://books.toscrape.com/catalogue/the-grand-design_405/index.html"

headers = {"Accept": "text/html", "User-Agent": "chrome"}
with request("GET", URL, headers=headers) as response:
    response.encoding = "uft-8"
    selector = Selector(text=response.text)


title = selector.css(".product_main h1::text").get()
price = selector.css(".product_main p.price_color::text").get()
description = (selector.css("#product_description ~ p::text").get()
               .removesuffix("...more").strip())


print({"título": title, "preço": price, "descrição": description, "url": URL})
