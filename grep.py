import re

fname = input('Nome do arquivo: ')
hand = open(fname)
comando = input('Comando: ')
cont = 0
for line in hand:
    line = line.rstrip()
    if re.search(comando, line):
        cont += 1
print("{} teve {} linhas que se igualam a {}".format(fname, cont, comando))