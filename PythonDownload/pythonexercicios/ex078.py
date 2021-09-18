a = []
maior = 0
menor = 0
for i in range(0, 5):
    a.append(int(input(f'Digite o numero da pocisão {i}º: ')))
    if i == 0:
        maior = menor = a[i]
    else:
        if a[i] > maior:
            maior = a[i]
        if a[i] < menor:
            menor = a[i]
print(f"numeros digitados: {a} ")
print(f'Maior numero digitado: {maior} menor numero digitado {menor}')
