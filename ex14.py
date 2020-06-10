"""
Encapsule esse código em uma função chamada contagem,
e generalize para que ela aceite a string e a letra como argumentos.
"""

palavra = input("Digite uma palavra: ").strip().lower()
letter = input("A letra da palavra anterior a ser contada: ").strip().lower()

def contagem(letra,string):
    contador = 0
    for l in string:
        if l == letra:
            contador = contador + 1
    print("Quantidade de letras '"'{}'"' é: {}".format(letra,contador))

contagem(letter,palavra)