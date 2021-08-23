n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
maior = 0
menu = 9
while menu != 0:
    menu = int(input('''Digite o numero da opção desejada: 
    1) Soma
    2) Multiplicar
    3) maior
    4) trocar numeros
    0) sair  '''))
    if menu == 1:
        print("a soma entre {} e {} é de".format(n1, n2), n1+n2)
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    elif menu == 2:
        print("Multiplicação entre {} e {} é de".format(n1, n2), n1*n2)
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    elif menu == 3:
        if n1 > n2:
            maior = n1

        else:
            maior = n2
        print("o maior numero é {}".format(maior))
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    elif menu == 4:
        n1 = int(input("Digite o primeiro numero para efetuar a troca: "))
        n2 = int(input("Digite o segundo numero para efetuar a troca: "))
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Fim do programa Obrigado!")
