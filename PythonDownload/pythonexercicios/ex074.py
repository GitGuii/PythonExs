from random import randint
maior = 0
menor = 0
n2 = (randint(0, 10), randint(0, 10), randint(
    0, 10), randint(0, 10), randint(0, 10))
print("Os valores sorteados foram os: ")
for c in n2:
    print(f"{c} ", end='')

print(
    f"\nDentre os numeros sorteados o maior numero foi {max(n2)} e o menor foi {min(n2)}")
