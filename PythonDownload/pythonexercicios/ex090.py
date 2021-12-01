nome = str(input('Digite o nome do aluno '))
nota = float(input(f'Media do {nome} '))
if nota <= 6.4:
    situ = 'Reprovado'
elif nota == 6.5:
    situ = 'Recuperação'
if nota > 6.5:
    situ = 'Aprovado'
media = {'nome':nome,'nota':nota,'Situação':situ}
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'aluno: {media["nome"]}')
print(f'media igual a: {media["nota"]}')
print(f'O aluno {media["nome"]} esta {media["Situação"]}')