"""
Escreva uma função chamada corte que recebe uma lista e
a modifica, removendo o primeiro e o último elemento, e retorna None.
Depois escreva uma função chamada meio que recebe uma lista e retorna
uma nova lista que contém todos, menos o primeiro e o último elemento.
"""
def corte(lista):
    tam = len(lista)
    valorF = lista[tam-1]
    lista.remove(lista[0])
    retorno = lista.remove(valorF)
    return retorno

def meio(lista):
    tam = len(lista)
    del lista[0::tam-1]
    return lista



l = ['a','b','d','e','f']

print(meio(l))