valor = int(input('Digite seu valor:\n'))
zero = valor
fatorial = 1

while zero > 0:
    print('{}'.format(zero), end=' ')
    print('x' if zero > 1 else '=', end=' ')

    fatorial = fatorial * zero
    zero -= 1
print(f'{fatorial}')

'''
Outra Forma Mais Acessível.
import math

num = int(input('Digite o seu valor:\n'))
f = math.factorial(num)
print('O fatorial de {}, é {}.'.format(num, f))

'''