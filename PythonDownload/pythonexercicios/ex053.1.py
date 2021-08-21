n1 = str(input("Digite uma palavra: ")).strip().upper()
palavras = n1.split()
juncao = ''.join(palavras)
inverso = juncao[::-1]
print("O inverso de {} é {} ".format(juncao, inverso))
if juncao == inverso:
    print("Portanto a palavra é um palindromo")
else:
    print('Portanto a palavra não é um palindromo')
