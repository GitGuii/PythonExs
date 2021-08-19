from datetime import date
atual = date.today().year
for c in range(1, 8):
    nasc = int(input('Digite os anos de nascimento {}: '.format(c)))
    idade = atual - nasc
    if idade < 18:
        menor = c
    elif idade >= 18:
        maior = c
print("quantidade de pessoas maiores de idade {}, quantidade de pessoas menores de idade {}".format(maior, menor))
