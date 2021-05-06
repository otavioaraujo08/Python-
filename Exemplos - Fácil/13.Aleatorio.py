import random

num_aleatorio = random.randint(0,5)
escolha = int(input('Escolha um valor entre 0 e 5:\n'))

if escolha == num_aleatorio:
    print(f'O número aleatório selecionado foi {num_aleatorio}, e sua escolha eh {escolha}')
    print('Você acertou :)')
else:
    print(f'O número aleatório selecionado foi {num_aleatorio}, e sua escolha eh {escolha}')
    print('Você errou :(')