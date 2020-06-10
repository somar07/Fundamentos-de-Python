"""
Adicione linhas de código no programa abaixo para iden-
tificar quem possui mais mensagens no arquivo. Após todo o dado ser
lido e todo o dicionário ser criado, procure no dicionário, utilizando um
laço máximo (Veja o capítulo 5: Laços máximo e mínimo), quem tem o
maior número de mensagens e mostre em tela quantas mensagens essa
pessoa tem.

"""
fname = input("Digite o nome do arquivo:")
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
def retornaDic(arquivo):
    counts = dict()
    for linha in arquivo:
        if linha.startswith('X-Authentication-Warning:'):#verifica qual linha inicia com o parametro passado
            palavras = linha.split() #coloca o conteúdo da linha em uma lista
            for word in palavras:
                if word == 'to':
                    pos = palavras.index(word) #Passando a posição da palavra 'para'
                    if palavras[pos+1] not in counts:
                        counts[palavras[pos+1]] = 1
                    else:
                        counts[palavras[pos+1]] += 1
    return counts

def maiorRecebedor(dicionario):
    Maior = None
    valor = 0 #Variavel para fins de comparação, pois os valores do dicionario estão todos em str
    for chave in dicionario:
        num = int(dicionario[chave])
        if Maior is None or num > valor:
            Maior = chave
            valor = int(dicionario[chave])
    
    print(Maior,dicionario[Maior])

dicio = retornaDic(fhand)
maiorRecebedor(dicio)