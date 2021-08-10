frase = input('digite uma frase qqr').upper().strip()
print('numero de letras A na frase: {}'.format(frase.count('A')))
print('Primeira letra A encontrada na frase foi na poçisão {} '.format(frase.find('A')+1))
print('Ultima letra A encontrada na frase foi na poçisão {} '.format(frase.rfind('A')+1))