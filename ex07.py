"""
Escreva um programa que solicite ao usuário uma tem-
peratura Celsius, converta para Fahrenheit, e mostre a temperatura
convertida.
"""

celsius = float(input("Digite a temperatura em Celsius: "))

fah = (celsius * 1.8) + 32

print("A temperatura em Fahrenheit é: {} ºF".format(fah))