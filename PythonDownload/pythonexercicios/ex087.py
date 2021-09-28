a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
coluna3 = maior = spar = 0
for l in range(0, 3):
    for c in range(0, 3):
        a[l][c] = int(input(f"Digite um valor para:[{l},{c}] "))

for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{a[l][c]:^5}]", end='')
        if a[l][c] % 2 == 0:
            spar += a[l][c]
    print()
print('-=' * 30)
print(f"a soma dos numeros pares é de : {spar}")
for l in range(0, 3):
    coluna3 += a[l][2]
print(f"soma da terceira coluna é de: {coluna3}")
for c in range(0, 3):
    if c == 0:
        maior = a[1][c]
    elif a[1][c] > maior:
        maior = a[1][c]
print(f'Maior numero na segunda linha é: {maior}')
