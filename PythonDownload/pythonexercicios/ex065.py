
resp = 'S'
media = 0
soma = qtde = maior = menor = 0
while resp in 'Ss':
    n1 = int(input("Digite um numero e digite "))
    soma = soma+n1
    qtde += 1
    if qtde == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
    resp = input("Deseja continuar? [S/N]")
media = soma/qtde
print("FIM, TOTAL DA MEDIA DOS NUMEROS DIGITADOS {}, maior numero {} menor numero {}".format(
    media, maior, menor))
