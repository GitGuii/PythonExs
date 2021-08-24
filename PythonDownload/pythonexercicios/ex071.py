print('='*60)
print('{:^30}'.format('Banco td3'))
print('='*30)
valor = int(input("Que valor voce quer sacar? R$ "))
total = valor
céd = 50
totalced = 0
while True:
    if total >= céd:
        total -= céd
        totalced += 1
    else:
        print(f'Total de {totalced} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totalced = 0
        if total == 0:
            break
print("Volte sempre :D")
