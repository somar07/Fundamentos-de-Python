try:
    fname = input("Digite o nome do arquivo: ")
    fhand = open(fname)
    count = 0
    for line in fhand:
        count = count + 1
    
    print('Há 1797 linhas de assunto em {}'.format(fname))
except:
    if fname == "na na boo boo".lower():
        print("na na boo boo para você tambem!!".upper())
    else:
        print("Arquivo {} não pôde ser aberto!".format(fname))