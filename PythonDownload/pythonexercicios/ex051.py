print('-='*15)
print('=='*15)
print('-='*15)
print("Progressão aritmética")
print('-='*15)
print('=='*15)
print('-='*15)

p = int(input("Primeiro termo: "))
r = int(input("Razão: "))
decimo = p + (10 - 1) * r
for c in range(p, decimo+r, r):
    print("{}".format(c), end='->')

print("Acabou")
