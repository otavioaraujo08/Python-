sem = 0
com = 0

for c in range(0,7):
    idade = int(input('Digite seu ano de nascimento:\n'))
    if 2021 - idade >= 18:
        print('Você eh maior de idade')
        com = com + 1
    else:
        print('Você eh menor de idade')
        sem = sem + 1
print('Pessoas maiores de idade: {}\nPessoas menores de idade: {}'.format(com, sem))
