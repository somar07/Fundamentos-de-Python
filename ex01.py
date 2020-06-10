"""
Exercícios:funções
1 -Crie uma função para desenhar uma linha, usando o caractere'_'.
O tamanho da linha deve ser definido na chamada da função.
"""

def linha(n):
    for i in range(n):
        print (end='_')
    print(" ")


l = int(input("Digite o tamanho da linha: "))
linha(l)