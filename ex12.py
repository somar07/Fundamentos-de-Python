"""
Escreva outro programa que pede por uma lista de números
como mostrada acima e mostra, no final, o máximo e o mínimo dos
números ao invés da média.
"""
minimo = None
maximo = None
while True:
    try:
        number = input("Digite um número: ")
        string = number
        number = int(number)
        if maximo is None or minimo is None:
            maximo = number
            minimo = number
        elif number < minimo:
            minimo = number
        elif number > maximo:
            maximo = number
    except:
        if string == 'pronto':
            break
        elif string != 'pronto':
            print("Entrada Inválida")

print("{} {}".format(minimo, maximo))