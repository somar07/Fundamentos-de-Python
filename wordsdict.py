"""
Escreva um programa que leia as palavras em words.txt e as armazena
como chaves em um dicionário. Não importa quais são os valores. Então,
você pode usar o operador in como uma maneira rápida de verificar se
uma string está no dicionário.
"""

fhand = open("words.txt")
dicionario = {}

for linha in fhand:
    palavras = linha.split()
    if len(palavras) == 0: continue
    for i in palavras:
        dicionario[i] = ' '

print(dicionario)