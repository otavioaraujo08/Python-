grupos = list()
mulheres = list()

grupo = dict()
idade_somada = 0
estatistica = {'pessoas_cadastradas': 0, 'media_idade': 0, 'acima_media': 0}

while True:
    grupo['nome'] = input('Digite o nome:\n')
    grupo['sexo'] = input('Digite o sexo: Apenas com M OU F\n').upper()
    while grupo['sexo'] not in 'FfMm':
        grupo['sexo'] = input('Digite o sexo: Apenas com M OU F\n').upper()
    if grupo['sexo'] in 'Ff':
        mulheres.append(grupo['nome'])
    grupo['idade'] = int(input('Digite a idade:\n'))

    grupos.append(grupo.copy())
    estatistica['pessoas_cadastradas'] += 1
    idade_somada += grupo['idade']
    estatistica['media_idade'] = idade_somada / estatistica['pessoas_cadastradas']
    if estatistica['media_idade'] < grupo['idade']:
        estatistica['acima_media'] += 1

    escolha = input('Quer continuar ? Apenas S ou N\n').upper()
    while escolha not in 'SsNn':
        escolha = input('Quer continuar ? Apenas S ou N\n').upper()
    if escolha in 'Nn':
        print(grupos)
        print(mulheres)
        print(estatistica)
        break