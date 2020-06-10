"""
Reescreva seu programa de cálculo de pagamento com um
1.5 o valor de hora de trabalho por hora extra, crie uma função chamada
calculoPagamento que aceita dois parâmetros(horas e TaxaHora).

Insira as Horas: 45
Insira o valor da Hora de Trabalho: 10
pagamento: 475.0
"""

def calculoPagamento(horas, TaxaHora):
    acrescimo = TaxaHora * 1.5
    if horas > 40:
        horas = horas * TaxaHora
        TaxaHora = TaxaHora + acrescimo
        print("Pagamento: {}".format(horas + TaxaHora))
    else:
        print("Pagamento: {}".format(horas*TaxaHora))
    

try:
    horas = int(input("Digite o valor das HORAS: "))
    taxa = float(input("Digite o valor da taxa: "))
    calculoPagamento(horas,taxa)     
except:
    print("Por utilize uma entrada numérica!")