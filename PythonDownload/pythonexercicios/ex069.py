c = 1
maior = 0
homem = 0
mulhermaior = 0
while True:
    idade = int(input("Digite a idade da {}° pessoa: ".format(c)))
    sexo = str(input("Digite o sexo da {}° pessoa M/F: ".format(c))).strip()
    print('====================================================================')
    c += 1
    if idade > 18:
        maior += 1
    if sexo in 'Mm': 
        homem += 1
    if sexo in 'Ff' and idade < 20:
        mulhermaior += 1
    continuar = str(input("Quer continuar sim ou nao? S/N "))
    print('====================================================================')
    print('====================================================================')
    if continuar in 'Nn':
        break
print(f'Quantidade de pessoas com mais de 18 anos {maior}')
print(f'Quantidade de homens foram cadastrados {homem}')
print(f'Mulheres com menos de 20 anos {mulhermaior}')
