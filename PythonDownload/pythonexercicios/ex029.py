n1 = int(input('Digite a velocidade do carro: '))
multa = (n1-80) * 7
if(n1>80):
    print('Carro acima da velocidade permitida valor da multa a pagar 7,00R$ pra cada km acima do limite')
    print('Valor da multa {}: '.format(multa))
else:
    print('Velocidade permitida')
