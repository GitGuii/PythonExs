
c = soma = 0
while True:
    n1 = int(input("Digite um numero, digite 999 para parar o programa: "))
    if n1 == 999:
        break
    c += 1
    soma += n1
print(f'Soma dos {c} valores foi {soma}')
