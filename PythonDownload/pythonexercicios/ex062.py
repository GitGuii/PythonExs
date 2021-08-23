p = int(input("Primeiro termo: "))
r = int(input("Razão: "))
c = 1
termo = p
qtde = 0
amais = 10
while amais != 0:
    qtde = qtde + amais
    while c <= qtde:
        print(termo, end=' ')
        termo += r
        c += 1
    amais = int(input("quantos termos vc quer a mais? "))
print("FIM")
print("Total de termos pedidos: {}".format(qtde))
