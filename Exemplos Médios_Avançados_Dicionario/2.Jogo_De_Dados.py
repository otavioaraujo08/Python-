import random
import time
import operator

jogadores = dict()

jogadores['jogador_um'] = random.randint(0, 10)
jogadores['jogador_dois'] = random.randint(0, 10)
jogadores['jogador_tres'] = random.randint(0, 10)
jogadores['jogador_quatro'] = random.randint(0, 10)

ranking = list()

print('x-x-x-x-x-x-x-x-')
for x, v in jogadores.items():
    print(f'Player {x} tirou {v} nos dados')
    time.sleep(1)
print('x-x-x-x-x-x-x-z-')

ranking = sorted(jogadores.items(), key=operator.itemgetter(1), reverse=True)

print('x-x-x-x-\nRanking\nx-x-x-x-')
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
    time.sleep(1)

