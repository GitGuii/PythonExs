num = int(input('Digite um numero entre 0 e 9999'))

if(num<=9999):
    u = num // 1 % 10
    d = num // 10 % 10
    c = num // 100 % 10
    m = num // 1000 % 10
    print('Analisando o numero {}'.format(num))
    print('unidade {}'.format(u))
    print('dezena {}'.format(d))
    print('centena {}'.format(c))
    print('milhar {}'.format(m))
else:
    print('numero maior')
