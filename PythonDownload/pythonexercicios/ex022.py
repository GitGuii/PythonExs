#frase = 'curso em video python'
#print(frase.count('o'))
#print(frase.replace('video','python'))
#print(frase.find('video'))
#dividido = frase.split()
#print(dividido)


nome = input('Digite o nome completo')
primeiro = nome.split()
divisao = nome.split()
juncao = ''.join(divisao)
maiusculo = (nome.upper())
minusculo = (nome.lower())
semespaco = (len(juncao))
pnome = (len(primeiro[0]))
print("Nome em letra maiuscula é {}".format(maiusculo))
print("Nome em minusculo é {}".format(minusculo))
print("Seu nome tem ao todo {} letras".format(semespaco))
print("Seu primeiro nome tem {} letras".format(pnome))



