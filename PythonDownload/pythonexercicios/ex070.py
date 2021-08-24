c = 1
mil = total = menor = 0
cont = 0
barato = ' '
while True:
    nome = str(input("Digite o nome do {}° produto: ".format(c)))
    preço = float(input("Digite o preço do {}° produto: ".format(c)))
    total += preço
    cont += 1
    if preço > 1000:
        mil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome
    c += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('fim do programa'))
print(f'O total da compra foi R${total:2.2f}')
print(f'Temos {mil} produtos com mais de R$1,000,00 reais')
print(f'O priduto mais barato foi {barato} que custa R${menor:2.2f}')
