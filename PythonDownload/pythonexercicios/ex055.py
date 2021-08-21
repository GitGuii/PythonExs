maior = 0
menor = 0
for c in range(0, 5):
    n1 = float(input("Digite o peso da {}° pessoa: ".format(c)))
    if c == 0:
        maior = n1
        menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
print("Dentre os 5 pesos citados acima o menor foi o de {} e o maior foi {}: ".format(menor, maior))
