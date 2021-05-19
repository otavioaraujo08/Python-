soma = media = mais_velho = menores_idade = 0
nome_velho = ''


for p in range(1, 5):
    print(F'-----Pessoa N: {p}-----')
    nome = str(input('Digite seu nome:\n'))
    idade = int(input('Digite sua idade:\n'))
    sexo = str(input('Digite seu sexo: [M/F]\n')).strip().upper()
    soma += idade
    if p == 1 and sexo in 'M':
        mais_velho = idade
        nome_velho = nome
    if sexo in 'M' and idade > mais_velho:
        mais_velho = idade
        nome_velho = nome
    if sexo in 'F' and idade < 20:
        menores_idade += 1

media = soma/4

print(F'Media de idade = {media}')
print(f'\nHomen mais velho: {nome_velho}.\nSua idade: {mais_velho}.')
print(f'\nNúmeros de mulheres mais novas: {menores_idade}.')