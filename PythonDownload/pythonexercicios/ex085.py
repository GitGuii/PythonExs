unica = [[], []]
for i in range(0, 7):
    n1 = int(input(f"Digite o {i+1}º numero"))
    if n1 % 2 == 0:
        unica[0].append(n1)
    else:
        unica[1].append(n1)
unica[0].sort()
unica[1].sort()
print(f"Numeros pares digitados: {unica[0]}")
print(f"Numeros impares digitados: {unica[1]}")
