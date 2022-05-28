from sys import argv


nome = ''
if len(argv) > 1:
    for index in range(1, len(argv)):
        if index > 1:
            nome += ' '
        nome += argv[index]
else:
    nome = input("Por favor, digite o seu nome:\n")

def triangle_name(name):
    result = name
    for index in range(len(name), 0, -1):
        print(name[0:index])

triangle_name(nome)
