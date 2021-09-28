a = []
cont = 1
maior = 0
menor = 0
while True:
    n1 = str(input(f"{cont}º Nome: "))
    peso = float(input(f"{cont}º Peso: "))
    b = [n1, peso]
    if len(a) == 0:
        maior = menor = b[1]
    else:
        if b[1] > maior:
            maior = b[1]
        if b[1] < menor:
            menor = b[1]
    a.append(b)
    b = str(input("Deseja continuar??: [S/N]"))
    if b in 'Nn':
        break
    else:
        cont += 1
print(f"Numero de pessoas cadastradas: {cont}")
print(f"O maior peso foi o de {maior}KG. Peso de: ", end='')
for i in a:
    if i[1] == maior:
        print(f"{i[0]} ", end='')
print()
print(f"O menor peso foi o de {menor}KG. peso de: ", end='')
for i in a:
    if i[1] == menor:
        print(f"{i[0]} ", end='')
