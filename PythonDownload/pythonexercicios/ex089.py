a = []
while True:
    nome = str(input('Nome '))
    nota1 = float(input('Nota 1 '))
    nota2 = float(input('Nota 2 '))
    media = (nota1 + nota2)/2
    a.append([nome, [nota1, nota2], media])
    n2 = str(input("Deseja continuar? [S/N]"))
    if n2 in 'Nn':
        break
print('-='*30)
print(f'{"No":<4}{"Nome":<10}{"Média":>8}')
print("-=" * 30)
for indice, aluno in enumerate(a):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
