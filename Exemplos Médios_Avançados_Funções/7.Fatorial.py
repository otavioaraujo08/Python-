from math import factorial


def fatorial(valor, show=False,):
    print(f'O fatorial eh igual a {valor}! ')
    f = 1
    for c in range(valor, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


valr = int(input('Digite o valor de fatorial:\n'))
resultado = fatorial(valr)

fatorial(resultado)