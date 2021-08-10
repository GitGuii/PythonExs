n1 = float(input('Digite a distância da viagem: '))
vc = n1 * 0.50
vl = n1 * 0.45
if(n1<=200):
    print('Valor da passagem {}:'.format(vc))
if(n1>200):
    print('valor da passagem {}'.format(vl))