import math

num1 = float(input("digite o valr do cateto oposto "))
num2 = float(input("digite o valor do cateto adjacente "))
hipo = math.hypot(num1,num2)
print("o comprimento da hipotenusa é {:.2f}".format(hipo))