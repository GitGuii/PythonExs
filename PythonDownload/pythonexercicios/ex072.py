while True:
    n1 = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
          'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
    n2 = int(input("Digite um numero entre 0 e 20: "))
    while n2 > 20:
        n2 = int(input("Tente novamente digite apenas numeros entre 0 e 20: "))
    n3 = n1[n2]
    print(f"Voçê digitou o numero {n3}")
    novamente = str(input("Quer rodar o programa novamente? ")).upper()
    if novamente in 'NAO':
        break
print("FIM")
