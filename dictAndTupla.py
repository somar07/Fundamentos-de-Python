"""
Revise um programa anterior como é pedido: Leia e analise
as linhas com “From” e retire os endereços dessas linhas. Conte o
número de mensagens de cada pessoa usando um dicionário. Depois de
todos os dados serem lidos, mostre a pessoa com mais envios criando
uma lista de tuplas (contagem, email) do dicionário. Então, ordene a
lista em ordem reversa e mostre a pessoa na primeira posição.
"""

fname = input("Digite o nome do arquivo: ")
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
counts = dict()
for linha in fhand:
    if linha.startswith('From:'):#verifica qual linha inicia com o parametro passado
        palavras = linha.split() #coloca o conteúdo da linha em uma lista
        for word in range(len(palavras)):
            if word == 1:#Passando a posição da palavra 'para'
                if palavras[word] not in counts:
                    counts[palavras[word]] = 1
                else:
                    counts[palavras[word]] += 1

list_tupla = list(counts.items())

def retorna_tupla(dicionario):
    lista = list()
    for name, value in dicionario.items():
        lista.append((value,name))
    lista.sort(reverse=True)
    x,y = lista[0]
    print('{} {}'.format(y,x))

retorna_tupla(counts)
