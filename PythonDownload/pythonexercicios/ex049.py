from time import sleep
n1 = int(input("Digite o numero que deseja ver a tabuada: "))
for c in range(0, 11):
    print("{} X {} = {}".format(n1, c, n1*c))
    sleep(1)
