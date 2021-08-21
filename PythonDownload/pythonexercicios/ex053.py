n1 = str(input("Digite uma palavra: ")).strip().upper()
palavras = n1.split()
juncao = ''.join(palavras)
inverso = ''
for c in range(len(juncao)-1, -1, -1):
    inverso += juncao[c]
print(juncao, inverso)
if juncao == inverso:
    print("é um palindromo")
else:
    print('Não é um palindromo')
