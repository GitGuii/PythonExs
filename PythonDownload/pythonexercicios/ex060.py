n1 = int(input("Digite um numero: "))
fat = n1
resul = 1
while fat > 0:
    print('{} '.format(fat), end='')
    print('x ' if fat > 1 else ' = ', end='')
    resul *= fat
    fat -= 1
print(resul)
print("fim")
