

def contador(inicio, fim, passo):
    print('-x' * 10)
    for a in range(1, 11):
        print(f'{a} ', end='')
    print()
    print('-x' * 10)
    for b in range(10, -1, -2):
        print(f'{b} ', end='')
    print()
    print('-x' * 10)
    for c in range(inicio, fim+1, passo):
        print(f'{c} ', end='')



zero = int(input('Digite o início da contagem:\n'))
um = int(input('Digite até que número você deseja parar:\n'))
dois = int(input('Digite o passo da contagem:\n'))

if dois == 0:
    dois += 1
if um < 0:
    um *= 1

contador(zero, um, dois)