jogador = dict()
partidas = list()

jogador['Nome'] = input('Digite o nome do jogador:\n')
jogador['Partidas'] = int(input('Quantas partidas ele jogou ?\n'))
jogador['Gols_Marcados'] = 0

for c in range(0, jogador['Partidas']):
    gol = int(input(f'Quantos gols ele marcou na partida {c}?\n'))
    jogador['Gols_Marcados'] += gol
print(jogador.items())