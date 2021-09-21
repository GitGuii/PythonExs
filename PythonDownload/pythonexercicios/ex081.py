a = []
while True:
    n1 = int(input("Digite um numero: "))
    a.append(n1)
    b = str(input("Deseja continuar? [S/N]"))
    if b in 'Nn':
        break
print(f"Quantidade de numeros digitados: {len(a)}")
a.sort(reverse=True)
print(f"Numeros digitados de forma decresente: {a}")
if 5 in a:
    print(f"Valor 5 esta na lista")
else:
    print("Valor 5 nao esta na lista")
