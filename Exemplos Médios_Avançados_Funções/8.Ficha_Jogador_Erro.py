def ficha(name, goals):
    print(f'O nome do jogador eh: {name}', end='\n')
    print(f'O número de gols: {goals}', end='\n')


nome = input('Digite o nome do jogador:\n')
gols = input('Digite quantos gols ele marcou:\n')

if nome == '':
    nome = '<DESCONHECIDO>'
if gols == '':
    gols = '<Desconhecido>'

ficha(nome, gols)