from time import sleep

def maior(* num):
    cont=maior = 0
    print('\nAnalisando Os Valores... ')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 5, 7, 11)

'''
Ou
def maior(val, maiooo):
    for c in range(len(val)):
        print(f'Valor: {val[c]} ', end='')
    print(f'\nO maior valor eh {maiooo}')


lista = [1, 3, 2, 5, 4]
big = 0

for a in range(len(lista)):
    if a < lista[a]:
        big = lista[a]

maior(lista, big)
'''