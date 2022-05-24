lista_dois = list(["dois", "two", "dos", 2])
tupla_dois = (enumerate(lista_dois))

for item in tupla_dois:
    print(len(item[1]))

# TypeError: object of type 'int' has no len()
