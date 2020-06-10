"""
Escreva um programa que leia um registro de mensagens,
construa um histograma, utilizando um dicionário, para contar quantas
mensagens chegaram em cada endereço de email e mostre em tela o
dicionário.

Enter a file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}

"""
fname = input("Digite o nome do arquivo:")
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
counts = dict()
for linha in fhand:
    if linha.startswith('From:'):#verifica qual linha inicia com o parametro passado
        palavras = linha.split() #coloca o conteúdo da linha em uma lista
        for word in palavras:
            if word == 'to':
                pos = palavras.index(word) #Passando a posição da palavra 'para'
                if palavras[pos+1] not in counts:
                    counts[palavras[pos+1]] = 1
                else:
                    counts[palavras[pos+1]] += 1
print(counts)
                

    