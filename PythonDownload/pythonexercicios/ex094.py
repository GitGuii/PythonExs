lista =list()
dic = dict()
somaidade = media = 0
mulher = []
acimamedia = []
while True:
    dic.clear()
    dic ['nome'] = str(input('Digite um nome: '))
    dic ['sexo'] = str(input('Qual o sexo: [M/F] '))
    while True:
        if dic['sexo'] not in 'MmFf':
            print('ERRO!! por favor digite apenas M ou F')
            dic ['sexo'] = str(input('Qual o sexo: [M/F] '))
        if dic['sexo'] in 'MmFf':
            break       
    dic ['idade'] = int(input('Digite a idade: '))
    lista.append(dic.copy())
    somaidade += dic['idade']
    media = somaidade/ len(lista) 
    if dic['sexo'] in 'Ff':
        mulher.append(dic['nome'])
    if dic['idade'] > media:
        acimamedia = dic['nome']
    cont = input('Quer continuar? [S/N]')
    if cont not in 'SsNn':
        print('ERRO!! por favor digite apenas S ou N')
        cont = input('Quer continuar? [S/N]')
    if cont in 'Nn' :
        break
print('Lista completa: ')
print('A) Quantidade de pessoas cadastradas: ',len(lista))
print('-=-=-=' * 30)
print(f'B) Media de idade das pessoas cadastradas: {media}')
print('-=-=-=' * 30)
print(f'C) Lista apenas com as mulheres: {mulher}')
print('-=-=-=' * 30)
if dic['idade'] < media:
    print('D) Não a pessoas com idade acima da media.')
if dic['idade'] > media:
    print(f' D) Lista de pessoas com idade acima da media: {acimamedia} ')