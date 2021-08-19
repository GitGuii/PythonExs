n1 = [input("Digite uma palavra")]
juncao = [''.join(n1)]


if juncao == juncao[-1]:
    print("Palavra digitada {}, é um palindromo!".format(n1))

print("palavra digitada {}, nao é um palindromo".format(n1))
