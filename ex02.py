"""
2 -Crie uma função que receba como parâmetro uma lista,com valores de qualquer tipo. 
A função deve imprimir todos os elementos da lista numerando-os.
"""

lista = [1, 2, 'a', 'b', 'c',20]

def enumera(l):
    contador = 0
    for x in l:
        contador =  contador + 1
        print('{}º) {}'.format(contador,x))

enumera(lista)

