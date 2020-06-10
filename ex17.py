fhand = input("Entre com o nome do arquivo: ")
fname= open(fhand)
count = 0
soma = 0
for line in fname:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        pontos = line.find(':')
        pos = len(line)
        host = line[pontos+1:pos]
        numero = float(host)
        soma = soma + numero
media = soma/count
print(media)

