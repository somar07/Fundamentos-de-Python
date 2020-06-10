"""
Reescreva o programa de notas do capítulo anterior us-
ando a função computarNotas que recebe a pontuação como parâmetro e
retorna a nota como uma string.
Pontuação   Nota
>= 0.9        A
>= 0.8        B
>= 0.7        C
>= 0.6        D
< 0.6         F

Digite a Pontuação: 0.95
A

Digite a Pontuação: perfeito
Pontuação Inválida

Digite a Pontuação: 10.0
Pontuação Inválida

Digite a Pontuação: 0.75
C

Digite a Pontuação: 0.5
F
"""

def computarNotas(pontos):
    if pontos >= 0.9 and pontos < 1.0:
        print("A")
    elif pontos >= 0.8 and pontos < 0.9:
        print("B")
    elif pontos >= 0.7 and pontos < 0.8:
        print("C")
    elif pontos >= 0.6 and pontos < 0.7:
        print("D")
    elif pontos < 0.6:
        print("F")
    else:
        print("Pontuação Inválida!")


try:
    pontuacao = float(input("Digite a Pontuação: "))
    computarNotas(pontuacao)
except:
    print("Pontuação Inválida!")