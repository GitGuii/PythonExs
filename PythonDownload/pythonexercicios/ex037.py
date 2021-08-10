n1 = int(input("Digite um numero: "))
print('''Escolha uma das bases para conversao:
[1] converter para binario
[2] converter para hexadecimal
[3] converter para octal''')
opcao = int(input("Sua opção: "))
if opcao == 1:
    print("{} convertido para BINARIO é igual a {}".format(n1, bin(n1)[2:]))
elif opcao == 2:
    print("{} convertido para HEXADECIAML é igual a {}".format(n1, hex(n1)[2:]))
elif opcao == 3:
    print("{} convertido para OCTADECIMAL é igual a {}".format(n1, oct(n1)[2:]))
else:
    print("Opção invalida, tente novamente")