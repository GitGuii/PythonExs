import math

angulo = float(input("Digite o angulo que voce deseja: "))
seno = math.sin(math.radians(angulo))
print("O seno do angulo {} é {} ".format(angulo,seno))
con = math.cos(math.radians(angulo))
print("o coseno do angulo {} é {} ".format(angulo,con))
tan = math.tan(math.radians(angulo))
print("A tangente do angulo {} é {} ".format(angulo,tan))