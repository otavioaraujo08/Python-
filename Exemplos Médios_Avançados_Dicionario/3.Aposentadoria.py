from datetime import datetime

pessoa = dict()

pessoa['nome'] = input('Digite o nome do individuo:\n')
pessoa['sexo'] = input('Qual o sexo do individuo ? Responder com M OU F.\n').upper()
nascimento = int(input('Em que ano você nasceu ?\n'))
pessoa['idade'] = datetime.now().year - nascimento
pessoa['carteira_trabalho'] = int(input('Digite o número da carteira se possuir:\n'))


if pessoa['carteira_trabalho'] == 0:
    print('\nx-x-x-x-x-x-')
    for c, v in pessoa.items():
        print(f'{c}: {v}')
    print('x-x-x-x-x-x-')
else:
    pessoa['ano_contratação'] = int(input('Digite o ano de contratação:\n'))
    pessoa['salario'] = float(input('Digite o salário dele:\n'))

    if pessoa['sexo'] in 'Mm':
        pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['ano_contratação'] + 35) - datetime.now().year)
    elif pessoa['sexo'] in 'Ff':
        pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['ano_contratação'] + 32) - datetime.now().year)
    else:
        print('Valor incorreto, tente novamente.')

    print('\nx-x-x-x-x-x-')
    for c, v in pessoa.items():
        print(f'{c}: {v}')
    print('x-x-x-x-x-x-')