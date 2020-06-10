"""
3 -Crie uma função que receba como parâmetro uma lista com valores 
numéricos e retorne a média desses valores.
"""

l = [1,2,3,4,5]

def soma_de_valores(lista):
    soma = 0
    for x in lista:
        soma = soma + x
    media = soma/len(lista)
    print('Média = {}'.format(media))

soma_de_valores(l)