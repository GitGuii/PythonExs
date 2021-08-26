timesg4 = ('Atlético mg', 'Palmeiras', 'Fortaleza', 'Bragantino')
time = 'Flamengo', 'Corinthians', 'Atletico GO', 'Ceara', 'Athletico PR', 'Internacional', 'Santos', 'São paulo', 'Juventude', 'Cuiaba', 'Bahia', 'Fluminense'
timesz4 = ('Gremio', 'Sport recife', 'America MG', 'Chapecoense')
todos = timesg4 + time + timesz4
print("-=-"*30)
print("-=-=-=-=-=-=-=Brasileirão 2021-=-=-=-=-=-=-=-=")
for c in todos:
    print(f"{c}")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("primeiros 4 colocados: ", timesg4)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("ultimos 4 colocados: ", timesz4)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print(f"Times em ordem alfabetica {sorted(todos)}")
print("-="*30)
print(f"A chapecoense esta na {todos.index('Chapecoense')+1}° posição")
