"""
Escreva um programa para abrir o arquivo chamado romeo.txt e leia-o linha por
linha. Para cada linha, separe-a em uma lista de palavras usando a função split.
Para cada palavra, cheque se esta palavra já existe na lista. Caso não exista,
adicione ela. Quando o programa terminar de verificar, ordene e imprima estas
palavras em ordem alfabética
"""

def retornaLista(arquivo):
    lista = []
    for linha in arquivo:
        palavras = linha.split()
        lista.extend(palavras)
    return lista

def palavrasOrdenadas(Nlista):
    tam = len(Nlista)
    listaFinal = []
    for i in range(tam):
        contador = Nlista.count(Nlista[i])
        if contador == 1:
            listaFinal.append(Nlista[i])
        elif contador > 1:
            ocorrencia = listaFinal.count(Nlista[i])
            if ocorrencia == 0:
                listaFinal.append(Nlista[i])
        contador = 0
    listaFinal.sort()
    return listaFinal

namef = input("Digite o nome do arquivo: ")
fhand = open(namef)
novaLista = retornaLista(fhand)
last = palavrasOrdenadas(novaLista)
print(last)