n1 = float(input('Digite seu peso: '))
n2 = float(input('Digite sua altura: '))
n3 = n2 * n2
imc = n1 / n3
print('De acordo com o seu peso {} e sua altura {} o seu imc é: {}'.format(n1,n2,imc))
if imc < 18.5:
    print('IMC Abaixo do peso')
elif imc == 18.5 or imc<=24.9:
    print('IMC peso ideal')
elif imc == 25 or imc<30:
    print('IMC sobrepeso')
elif imc ==30 or imc<=40:
    print('IMC obesidade')
else:
    print('IMC obesidade morbida')