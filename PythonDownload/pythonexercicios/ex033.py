n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
if(n1>n2 and n1>n3):
    print('O maior numero foi o {}:'.format(n1))
if(n2>n3 and n2>n1):
    print('O maior numero foi o {]:'.format(n2))
if(n3>n2 and n3>n1):
    print('O maior numero foi o {}:'.format(n3))
if(n1<n2 and n1<n3):
    print('O menor numero é o {}'.format(n1))
if(n2<n1 and n2<n3):
    print('O menor numero é o {}'.format(n2))
if(n3<n2 and n3<n1):
    print('O menor numero é o {}'.format(n3))
