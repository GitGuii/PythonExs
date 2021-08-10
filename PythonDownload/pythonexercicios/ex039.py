Idade = int(input('Digite a idade do jovem: '))

if Idade < 18:
    print('Ainda nao esta na hora de se alistar...')
    prazo = 18 - Idade
    print('Faltam {} anos para o alistamento'.format(prazo))
elif Idade ==18:
    print('Esta na hora de se alistar')
elif Idade >18:
    print('Ja passou da idade de alistamento')
    prazo = Idade - 18
    print('Já se passaram {} anos do prazo de alistamento'.format(prazo))