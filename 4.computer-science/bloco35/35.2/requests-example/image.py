import requests


# Requisição a recurso binário
response = requests.get("http://httpbin.org/image/png")
with open("pig.png", "w+b") as file:
    file.write(response.content)
