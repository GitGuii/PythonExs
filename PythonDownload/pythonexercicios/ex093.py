dados = dict()
total = 0
dados ['nome'] = str(input('Nome do jogador: '))
dados ['jogos']= int(input(f'quantos jogos {dados["nome"]} tem: '))
for i in range(0,dados['jogos']) :
    i += 1
    gols = int(input(f'Quantos gols na {i}° partida: '))
    total += gols

dados ['gols']= total
for k,v in dados.items():
    print(f'{k}: {v}')

