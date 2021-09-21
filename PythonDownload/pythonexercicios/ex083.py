a = str((input("Digite a expressão matematica: ")))
p = []
for i in a:
    if i == '(':
        p.append('(')
    elif i == ')':
        if len(p) > 0:
            p.pop()
        else:
            p.append(')')
            break
if len(p) == 0:
    print("Sua expressão esta valida!!")
else:
    print("Sua expressão esta invalida")
