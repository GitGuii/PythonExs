p = int(input("Primeiro termo: "))
r = int(input("Razão: "))
c = 1
termo = p
while c <= 10:
    print(termo)
    termo += r
    c += 1
print("fim")
