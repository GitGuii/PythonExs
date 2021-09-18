a = []
while True:
    n1 = int(input("Digite um valor: "))
    if n1 not in a:
        a.append(n1)
        print("numero adicionado com sucesso...")
    else:
        print("Valor duplicado!! Nao irei adicionar...")
    b = str(input("Quer continuar? [S/N]"))
    if b in 'nN':
        break
a.sort()
print(a)
