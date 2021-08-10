print('{:=^40}'.format(" Organizações tabajaras "))
preco = float(input("preço das compras: R$ "))
print('''formas de pagamento 
[1] A vista dinheiro/cheque
[2] A vista no cartão
[3] 2x no cartão
[]4 3x ou mais no cartão''')
opcao = int(input("Digite a opção de pagamento "))
if opcao == 1:
    total = preco - (preco *10/100)
elif opcao == 2:
    total = preco -(preco *5/100)
elif opcao == 3:
    total = preco
    parcela = preco / 2
    print('Sua compora de {} sera parcelada em 2x de {:.2f}'.format(preco,parcela))
elif opcao == 4:
    total = preco + (preco *20/100)
    totparcelas = int(input("Quantas parcelas? "))
    parcela = total / totparcelas 
    print("sua compra sera parcelada em {} vezes de {:.2f} com juros".format(totparcelas,parcela))
print('Sua compra  de  {:.2f} vai custar {:.2f} no final'.format(preco, total))


