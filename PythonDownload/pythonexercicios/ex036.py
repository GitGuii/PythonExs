vcasa = float(input('Digite o valor da casa'))
sal = float(input('Digite o valor do salario'))
anoqtd = float(input('Em quantos anos sera pago'))
ano = anoqtd * 12
pres = vcasa/ano
vaprov = sal * 30 /100
if pres < vaprov:
    print('De acordo com o valor da casa {:.2f} em {} anos a prestação sera de {:.2f}'.format(vcasa,anoqtd,pres))
    print("Emprestimo aprovado")
else:
    print('De acordo com o valor da casa {:.2f} em {} anos a prestação sera de {:.2f}'.format(vcasa, anoqtd, pres))
    print('Emprestimo negado')
