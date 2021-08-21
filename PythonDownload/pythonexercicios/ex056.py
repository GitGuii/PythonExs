somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
idademeninas = 0
for c in range(1, 5):
    nome = str(input("Digite o nome da {}° pessoa: ".format(c))).strip()
    idade = int(input("Digite a idade da {}° pessoa: ".format(c)))
    sexo = str(input("Digite o sexo da {}° pessoa M/F: ".format(c))).strip()
    print("-------------------------------------------------")
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if idade < 20 and sexo in 'Ff':
        idademeninas += 1
mediaidade = somaidade/4
print("A media de idade das pessoas é de {}".format(mediaidade))
print("Nome do homem mais velho {}".format(nomevelho))
print("Quantidade de meninas com menos de 20 anos: {}".format(idademeninas))
