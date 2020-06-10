"""
Escreva um programa que peça por uma pontuação entre
0.0 e 1.0. Se a pontuação for fora do intervalo, mostre uma mensagem
de erro. Se a pontuação estiver entre 0.0 e 1.0, mostre a respectiva nota
usando a seguinte tabela
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

Rode o programa repetidamente como mostrado acima para testar diferentes valores de entrada.
"""

try:
    pontuacao = float(input("Digite a Pontuação: "))
    if pontuacao >= 0.9 and pontuacao < 1.0:
        print("A")
    elif pontuacao >= 0.8 and pontuacao < 0.9:
        print("B")
    elif pontuacao >= 0.7 and pontuacao < 0.8:
        print("C")
    elif pontuacao >= 0.6 and pontuacao < 0.7:
        print("D")
    elif pontuacao < 0.6:
        print("F")
    else:
        print("Pontuação Inválida!")
except:
    print("Pontuação Inválida!")