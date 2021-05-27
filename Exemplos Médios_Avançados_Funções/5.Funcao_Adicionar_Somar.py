from random import randint

numeros = list()

def sorteio(lista):
    for c in range(0, 5):
        valor = randint(0, 6)
        lista.append(valor)
    print(f'Valores da lista: {lista}')
    print('-x' * 10)


def somar(listaa):
    soma = 0
    for a in range(len(listaa)):
        if listaa[a] % 2 == 0:
            soma += listaa[a]
    print(f'A soma dos valores PARES da Lista: {listaa}.\nResultado: {soma}')


sorteio(numeros)
somar(numeros)