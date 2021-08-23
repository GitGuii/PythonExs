sexo = str(input("Digite o sexo: F/M ")).strip().upper()
while sexo not in 'MmFf':
    sexo = str(input("Digite apenas F ou M: "))
print(sexo)
