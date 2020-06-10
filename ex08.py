"""
Reescreva seu programa de pagamento, para pagar ao fun-
cionário 1.5 vezes o valor da taxa horária de pagamento pelo tempo
trabalhado acima de 40 horas

Digite as Horas: 45
Digite a taxa: 10
Pagamento: 475.0
"""

horas = int(input("Digite o valor das HORAS: "))
taxa = float(input("Digite o valor da taxa: "))
acrescimo = taxa * 1.5

if horas > 40:
    horas = horas * taxa
    taxa = taxa + acrescimo
    print("Pagamento: {}".format(horas + taxa))
else:
    print("Pagamento: {}".format(horas*taxa))

