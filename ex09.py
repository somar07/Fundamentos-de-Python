try:
    horas = int(input("Digite as HORAS: "))
    taxa = float(input("Digite a TAXA: "))
 
    valor = horas * taxa
    print("O valor a ser pago: {}".format(valor))
except:
    print("Por utilize uma entrada numérica!")