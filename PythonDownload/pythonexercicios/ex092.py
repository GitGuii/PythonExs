from datetime import datetime
dados = dict()
dados ['Nome'] = str(input('Digite o nome: '))
nasc = int(input('Digite a data de nascimento: '))
dados ['idade'] = datetime.now().year - nasc
dados ['CTPS'] = int(input('Carteira de trabalho (0 caso nao tenha: '))
if dados ['CTPS'] != 0:
    dados ['contratação'] = int(input('Ano de contratação'))
    dados ['salario'] = float(input('salario: R$'))
    dados ['Aposentadoria'] = dados ['idade'] + ((dados ['contratação'] + 35) - datetime.now().year)
print ('-='* 30)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')