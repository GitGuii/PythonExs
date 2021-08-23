n1 = int(input("quantos termos fibonacci vc quer ver?: "))
c = 3
fibo1 = 0
fibo2 = 1
while c <= n1:
    fibo = fibo1 + fibo2
    print("-> {}".format(fibo), end='')
    fibo1 = fibo2
    fibo2 = fibo
    c += 1
print("-> FIM")
