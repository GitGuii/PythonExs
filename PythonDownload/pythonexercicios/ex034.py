n1 = float(input('Digite o salario do funcionario: '))
s1 = 10 * n1
de = s1/100
dez = n1 + de
s = 15 * n1
des = s/100
quinze = n1 + des
if(n1>1250):
    print('Valor do salario {}, Valor do salario com o aumento de 10% {}'.format(n1,dez))
if(n1<=1250):
    print('Valor do salario {}, Valor do salario com o aumento de 15% {}'.format(n1, quinze))