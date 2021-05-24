time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = input('Nome do jogador:\n')
    total = int(input(f'Quantas partidas {jogador["nome"]} disputou ?\n'))
    partidas.clear()

    for c in range(0, total):
        partidas.append(int(input(f'Quantos gols foram marcados na partida {c+1} ?\n')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        escolha = input('Quer continuar ? S ou N').upper()[0]
        if escolha in 'SsNn':
            break
        print('Comando incorreto ! Responda apenas com S oou N.')
    if escolha == 'N':
        break
print('-x-x-x-x-x-x-x')
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-x-x-x-x-x-x-x')

for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-x-x-x-x-x-x-x')
while True:
    busca = int(input('Mostrar dados na tabela de que jogador ? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Não existe jogador com o código {busca}!')
    else:
        print(f'-- Estatísticas do jogador: {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-x-x-x-x-x-x-x-x')
print(' Volte sempre :)')