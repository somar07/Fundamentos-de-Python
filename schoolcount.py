"""
Esse programa grava o domínio de email (ao invés do en-
dereço) de onde a mensagem foi enviada ao invés de quem o email veio (
i.e., o endereço completo da mensagem). No final do programa, mostre
em tela o conteúdo do seu dicionário.
"""

 
def retornaLista(arquivo):
    listNames = []
    for line in arquivo:
        if line.startswith('Author:'):#verifica qual line inicia com o parametro passado
            palavras = line.split() #coloca o conteúdo da line em uma lista
            for word in range(len(palavras)):
                if word == 1:
                    palavra = list(palavras[word])
                    for c in palavra:
                        if c == '@':
                            posicao = palavra.index(c)
                            stringF = ''.join(palavra)[posicao+1:]
                            listNames.append(stringF)
    return listNames

def retornaDicionario(lista):
    counts = dict()
    for word in lista:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
    return counts


fname = input("Digite o nome do arquivo:")
try:
    file = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

lista = []
lista = retornaLista(file)
print(retornaDicionario(lista))
