from  datetime import date
n1 = int(input('Digite um ano ou digite 0 para analisar um ano atual '))
if n1==0:
    n1 = date.today().year
if(n1%4==0 and n1%100 !=0 or n1%400==0):
    print('o ano {} é bissexto'.format(n1))
else:
    print('Ano {} nao é bissexto'.format(n1))

