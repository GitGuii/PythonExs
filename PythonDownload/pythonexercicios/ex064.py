cont = soma = n1 = 0
n1 = int(input("Digite um numero e digite [999] para parar o programa "))
while n1 != 999:
    soma += n1
    cont += 1
    n1 = int(input("Digite um numero e digite [999] para parar o programa"))
print("Fim do programa, total de numero digitados {} soma dos numeros digitados {} ".format(cont, soma))
