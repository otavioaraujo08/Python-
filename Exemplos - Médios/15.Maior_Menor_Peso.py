maior = menor = 0

for c in range(1,7):
    peso = float(input('Digite seu peso:\n'))

    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < maior:
            menor = peso

print(f'Maior: {maior}.\nMenor: {menor}.')
