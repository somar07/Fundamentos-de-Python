"""
Escreva um programa que solicite ao usuário as horas e o
valor da taxa por horas para calcular o valor a ser pago por horas de
serviço.
"""
horas = int(input("Digite as HORAS: "))
taxa = float(input("Digite a TAXA: "))

valor = horas * taxa

print("O valor a ser pago: {}".format(valor))