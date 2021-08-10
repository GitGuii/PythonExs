from datetime import date 
atual = date.today().year
nasc = int(input('Digite o ano de nascimento do jovem: '))
Idade = atual - nasc
print("Quem nasceu em {} tem {} anos em {}".format(nasc,Idade,atual))
if Idade < 18:
    print('Ainda nao esta na hora de se alistar...')
    prazo = 18 - Idade
    print('Faltam {} anos para o alistamento'.format(prazo))
    ano = prazo + atual
    print("Seu alistamento sera em {}".format(ano))
elif Idade == 18:
    print('Esta na hora de se alistar!!')
elif Idade > 18:
    print('Ja passou da idade de alistamento')
    prazo = Idade - 18
    print('Já se passaram {} ano(s) do prazo de alistamento'.format(prazo))
    ano = prazo - atual
    print("O ano para alistamento foi em {}".format(ano))