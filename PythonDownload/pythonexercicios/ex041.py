from datetime import date, datetime
atual = datetime.today().year
nascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = atual - nascimento
if idade <= 9:
    print('Atleta mirim.')
elif idade > 9 and idade<= 14:
    print('Atleta infantil.')
elif idade >14 and idade<=19:
    print('Atleta junior.')
elif idade >19 and idade<=20:
    print('Atleta senior.')
else:
    print('Atleta master.')