a = []
impar = []
par = []
while True:
    n1 = int(input("Digite um valor: "))
    a.append(n1)
    if n1 % 2 == 0:
        par.append(n1)
    elif n1 % 2 != 0:
        impar.append(n1)
    s = str(input("Deseja continuar? [S/N]"))
    if s in 'Nn':
        break
print(f"Lista geral {a}")
print(f"Lista dos pares {par}")
print(f"Lista dos impares {impar}")
