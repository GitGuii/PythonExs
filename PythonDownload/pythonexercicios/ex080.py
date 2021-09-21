a = []
for i in range(0, 5):
    n = int(input(f"Digite o {i+1}º numero: "))
    if i == 0 or n > a[len(a)-1]:
        print(f'Ultimo valor adicionado')
        a.append(n)
    else:
        pos = 0
        while pos < len(a):
            if n <= a[pos]:
                a.insert(pos, n)
                print(f'Adicionado na pocisão {pos+1} da lista...')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {a}')
