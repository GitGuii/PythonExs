soma = 0
for c in range(1, 7):
    i = int(input("Digite o {} valor ".format(c)))
    if i % 2 == 0:
        soma = soma + i

print("dos {} digitados a soma dos numero PARES foi de {}".format(c, soma))
