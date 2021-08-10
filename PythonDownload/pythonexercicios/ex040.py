n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
m = (n1 + n2)/2
if m < 5.0:
    print('Aluno reprovado :(')
elif m == 5.0 and 6.9:
    print('Aluno de recuperação')
elif m > 7.0:
    print('Aluno aprovado :D')