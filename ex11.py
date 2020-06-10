"""
Escreva um programa que lê repetitivamente números até
que o usuário digite “pronto”. Quando “pronto” for digitado, mostre a
soma total, a quantidade e a média dos números digitados. Se o usuário
digitar qualquer coisa que não seja um número, detecte o erro usando
o trye o except e mostre na tela uma mensagem de erro e pule para o
próximo número.


Digite um número: 4
Digite um número: 5
Digite um número: dado errado
Entrada Inválida
Digite um número: 7
Digite um número: pronto
16 3 5.333333333333333
"""
cont = 0
soma = 0
while True:
    try:
        number = input("Digite um número: ")
        string = number
        cont = cont + 1
        soma = soma + int(number)
    except:
        if string == 'pronto':
            cont = cont - 1
            break
        elif string != 'pronto':
            cont = cont - 1
            print("Entrada Inválida")
print("{} {} {}".format(soma, cont, soma/cont))



    