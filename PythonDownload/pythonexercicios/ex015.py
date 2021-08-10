km = float(input("quantos kms percorridos? "))
dias= float(input('quantos dias de uso? '))
valordia = dias * 60
valorkm = km * 0.15
total = valordia + valorkm
print('o aluguel do carro ficou: {}'.format(total))
