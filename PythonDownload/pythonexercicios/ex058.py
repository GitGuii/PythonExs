import random
n1 = int(input('Em que numero eu pensei entre 0 e 10: '))
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n2 = random.choice(lista)
c = 0
if n1 == n2:
    print('Voçê escolheu o numero da maquina!!')
    print("numero de tentativas {}".format(c))
else:
    while n1 != n2:
        print("------------------------------")
        print('Perdeu !!! eu pensei no numero {} e nao no {}: '.format(n2, n1))
        print("------------------------------")
        c += 1
        n2 = random.choice(lista)
        n1 = int(input('Em que numero eu pensei entre 0 e 10: '))
print("digitei {} e vc {} parabens acertou o meu numero !!!".format(n2, n1))
print("Tentativas ate acertar : {}".format(c))
