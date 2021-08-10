import random

n =(input('Digite:\n 01 para pedra \n 02 para papel \n 03 para tesoura: '))
n1 = "pedra"
n2 = "papel"
n3 = "tesoura"
lista = [n1,n2,n3]
nr = random.choice(lista)
if n==1 and nr==n1 or n==2 and nr==n2 or n==3 and nr==n3:
    print('Empate!!')
elif n1 == 1 and nr ==n2:
    print('Voçê escolheu pedra e a maquina escolheu papel...')
    print('Vitoria da maquina!!!')
elif n1 == 1 and nr == n3:
    print('Voçê escolheu pedra e a maquina escolheu tesoura...')
    print('Voçê venceu!!!')
elif n1 == 2 and nr == n1:
    print('Voçê escolheu papel e a maquina escolheu pedra')
    print('Voçê venceu!!!!!!')
elif n1 == 2 and nr == n3:
    print('Voçê escolheu papel e a maquina escolheu tesoura')
    print('Vitoria da maquina!!!')
elif n1 == 3 and nr == n1:
    print('Voçê escolheu tesoura e a maquina escolheu pedra')
    print('Vitoria da maquina!!!')
elif n1 == 3 and nr == n2:
    print('Voçê escolheu tesoura e a maquina escolheu papel')
    print('Voçê venceu!!!!!!')
