"""
Utilize o seguinte código em Python que guarda uma string:
str = 'X-DSPAM-Confidence:0.8475' Use a função find e o fatiamento de
strings para extrair a porção da string depois do sinal de dois pontos e
use a função float para converter a string extraída em um número de
ponto flutuante.
"""
data = 'X-DSPAM-Confidence:0.8475'

antscaract = data.find(':')
poscaract = len(data)

host = data[antscaract+1:poscaract]
host = float(host)
print(host)