idade = int(input('Digite a idade do atleta: '))
if idade <= 9:
    print('Atleta mirim.')
elif idade > 9 or <= 14:
    print('Atleta infantil.')
elif idade >14 or <=19:
    print('Atleta junior.')
elif idade >19 or <=20:
    print('Atleta senior.')
else:
    print('Atleta master.')