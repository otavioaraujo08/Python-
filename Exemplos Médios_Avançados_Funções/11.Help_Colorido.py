c = ('\033[m', '\033[0;30;41m', '\33[0;30;42m', '\33[0;30;43m',)


def ajuda(esc):
    titulo(f'Acessando o manual do comando \'{esc}\'', 3)
    print(c[1], end='')
    help(esc)


def titulo(msg, cor=0):
    tam = len(msg)
    print(c[cor], end='')
    print('-x' * tam)
    print(msg)
    print('-x' * tam)
    print(c[0], end='')


while True:
    titulo('Sistema de ajuda PyHelp', 2)
    comando = input('Função ou Biblioteca:\n')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até Logo!', 1)