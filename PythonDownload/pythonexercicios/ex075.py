
n1 = (int(input("Digite um numero: "))), (int(input("Digite outro numero: "))), (
    int(input("Digite outro numero: "))), (int(input("Digite o ultimo numero: ")))

print(f"Voçê digitou os numeros {n1}")
print(f"O numero 9 apareceu {n1.count(9)} vezes")
if 3 in n1:
    print(f"O numero 3 apareceu na {n1.index(3)+1}° poçisão")

else:
    print("nao foi digitado o numero 3")
print("Os valores pares digitados foram ", end='')
for n in n1:
    if n % 2 == 0:
        print(n, end=' ')
