import random
V = 0
while True:
    print("-------jogo do par ou impar-------")
    m1 = str(input("Voçê quer par ou impar!?!? "))
    n1 = int(input("Digite um numero..."))
    n2 = int(random.randint(0, 10))
    if m1 in 'parPAR':
        resultado = n1 + n2
        if resultado % 2 == 0:
            V += 1
            print(f'Maquina escolheu o numero {n2}, e vc o {n1}...')
            print("---------DEU PAR----------------")
            print("Parabéns!!! voçê pediu par e ganhou")
            print("-------------------------------------")
        if resultado % 2 != 0:
            print(f'Maquina escolheu o numero {n2}, e vc o {n1}...')
            print("---------DEU IMPAR----------------")
            print("NAO FOI DESSA VEZ!!! voçê pediu par e PERDEU")
            break
    else:

        if m1 in 'imparIMPAR':
            resultado = n1 + n2
            if resultado % 2 != 0:
                V += 1
                print(f'Maquina escolheu o numero {n2}, e vc o {n1}...')
                print("---------DEU IMPAR--------------")
                print("Parabéns!!! Voçê pediu impar e ganhou")
                print("-------------------------------------")
            if resultado % 2 == 0:
                print(f'Maquina escolheu o numero {n2}, e vc o {n1}...')
                print("---------DEU PAR--------------")
                print("NAO FOI DESSA VEZ!!! Voçê pediu impar e PERDEU")
                break

print("fim do programa")
print(f'Voçê saiu vencedor {V} vezes')
