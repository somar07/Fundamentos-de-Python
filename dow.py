"""
Escreva um programa que categorize cada mensagem de
e-mail de acordo com o dia em que a mensagem foi enviada. Para
isso, procure por linhas que comecem com “From”, depois procure pela
terceira palavra e mantenha uma contagem de ocorrência para cada dia
da semana. No final do programa, mostre em tela o conteúdo do seu
dicionário (a ordem não interessa).
linha exemplo:

From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

Exemplo de código:
python dow.py
Enter a file name: mbox-short.txt
{'Sex': 20, 'Qui': 6, 'Sab': 1}
"""

fname = input("Digite o nome do arquivo:")
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
counts = dict()
for linha in fhand:
    if linha.startswith('From'):
        palavras = linha.split()
        for word in range(len(palavras)):
            if word == 2:
                if palavras[word] not in counts:
                    counts[palavras[word]] = 1
                else:
                    counts[palavras[word]] += 1
print(counts)
    