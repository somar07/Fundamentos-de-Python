"""
Escreva um loop while que inicia no último caractere da
string e caminha para o primeiro caractere, imprimindo cada letra em
uma linha separada.
"""

string = "Rafael"
indice = len(string)
"""
while indice > 0:
    letra = string[indice-1]
    print(letra)
    indice = indice - 1
"""
for char in range(len(string))[::-1]:
    print(string[char])
 