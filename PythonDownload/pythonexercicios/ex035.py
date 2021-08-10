n1 = float(input('Digite o primeiro numero'))
n2 = float(input('Digite o segundo numero'))
n3 = float(input('Digite o terceiro numero'))
if n1 < (n2 + n3) and n2 < (n1 + n3) and n3 < (n2 + n1):
    print('Podem formar um triangulo')
else:
    print('Nao formam um triangulo')
