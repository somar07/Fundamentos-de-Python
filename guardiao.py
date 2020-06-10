"""
Descubra qual linha do programa acima não está devida-
mente protegida. Veja se você pode construir um arquivo de texto que
causa falha no programa e depois modifique o programa para que a
linha seja propriamente protegida e por fim, teste o programa para ter
certeza que ele manipula corretamente o novo arquivo de texto.

Exercício 3: Reescreva o código guardião nos exemplos acima sem duas
declarações if. Em vez disso, use uma expressão lógica composta usando
o operador lógico and, com uma única declaração if.

fhand = open('teste.txt')
for linha in fhand:
    palavras = linha.split()
    # print 'Debug:', palavras
    if len(palavras) == 0 : continue
    if palavras[0] != 'From' or len(palavras) == 1: continue
    print(palavras[2])
"""
#Exercício 3
fhand = open('mbox-short.txt')

for linha in fhand:
    palavras = linha.split()
    if len(palavras) == 0 or palavras[0] != 'From': continue
    print(palavras[2])