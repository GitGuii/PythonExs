lista = ('caderno', 15.00,
         'lapis', 1.75,
         'borracha', 0.50,
         'caneta', 1.50)
print('-'*50)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*50)
for item in range(len(lista)):
    if item % 2 == 0:
        print(f"{lista[item]:.<30}", end='')
    else:
        print(f"R${lista[item]:>7.2f}")
