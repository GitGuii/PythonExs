
while True:
    resultado = 0
    n1 = int(input("Digite o numero que deseja ver a tabuada: "))
    c = 0
    if n1 < 0:
        break
    while c <= 10:
        resultado = n1 * c
        print(f'{n1} x {c} = {resultado}')
        c += 1
print("FIM")
