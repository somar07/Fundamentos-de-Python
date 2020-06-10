import re

fname = input("Arquivo de entrada: ")
hand = open(fname)
soma = 0
cont = 0

for line in hand:
    line = line.rstrip()
    x = re.findall('^New Revision\S*: ([0-9.]+)', line)
    if len(x) > 0:
        numero = ''.join(x)
        real = float(numero)
        soma += real
        cont += 1

media = soma/cont
print(media)