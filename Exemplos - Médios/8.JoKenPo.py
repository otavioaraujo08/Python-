import random

print('Jokenpo: Escolha:\n1 para pedra.\n2 para tesoura.\n3 para papel')
escolha = int(input('Escolha entre 1 e 3:\n'))
cpu = random.randint(1, 3)

if escolha == 1 and cpu == 2 or escolha == 2 and cpu == 3 or escolha == 3 and cpu == 1:
    print(f'HUMAN WINS: {escolha}\nCPU LOSE: {cpu}')
elif cpu == 1 and escolha == 2 or cpu == 2 and escolha == 3 or cpu == 3 and escolha == 1:
    print(f'CPU WINS: {cpu}\nHUMAN LOSE: {escolha}')
else:
    print(f'Empate:\nHUMAN: {escolha}.\nCPU: {cpu}.')
