import random

n1 = "gui"
n2 = "maria"
n3 = "joao"
n4 = "jose"
lista = [n1,n2,n3,n4]
print("Dentre os alunos {}, {}, {}, {}, o aluno {} foi o premiado para apagar o quadro".format(n1,n2,n3,n4,random.choice(lista)))