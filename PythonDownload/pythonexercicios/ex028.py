#n1 = float(input('Digite um numero: '))
#n2 = float(input('Digite um numero: '))
#cal = int(input('Digite 1 se quiser somar \n Digite 2 se quiser subtrair \n Digite 3 se quiser multiplicar \n Digite 4 se quiser dividir: '))
#soma = n1 +n2
#sub = n1-n2
#mult = n1*n2
#div = n1/n2
#if (cal ==1):
#    print('A soma é {}'.format(soma))
#if(cal==2):
#    print('A subtração é {}'.format(sub))
#if(cal==3):
#    print('A multiplicação é {}'.format(mult))
#if(cal==4):
#    print('A divisão é {}'.format(div))
#if(cal>4):
#    print('Opção inexistente.')
#if(cal<1):
#    print('Opção inexistente.')
import random

n1 = int(input('Em que numero eu pensei entre 0 e 5: '))
lista = [0,1,2,3,4,5]
n2 = random.choice(lista)
if n1==n2:
    print('Voçê escolheu o numero da maquina!!')
else:
    print('Eu ganhei!!! eu pensei no numero {} e nao no {}: '.format(n2,n1))


