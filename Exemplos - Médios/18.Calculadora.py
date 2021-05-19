valor_um = int(input('Digite seu primeiro valor:\n'))
valor_dois = int(input('Digite seu segundo valor:\n'))
ficha = 5
escolha_um = escolha_dois = 0

while ficha == 5:
    print('Seu números escolhidos foram: {} e {}\n'
    'Escolha uma Opção:\n'
    '[1] Somar\n'
    '[2] Multiplicar\n'
    '[3] Maior\n'
    '[4] Novos números\n'
    '[5] Sair do programa'.format(valor_um, valor_dois))
    escolha = int(input('FAÇA SUA ESCOLHA PILANTRA.\n'))

    if escolha == 1:
        print(f'A soma de {valor_um} e {valor_dois} é igual a: {valor_um + valor_dois}\n')
        ficha = 5

    elif escolha == 2:
        print(f'A multiplicação de {valor_um} e {valor_dois} é igual a: {valor_um * valor_dois}\n')
        ficha = 5

    elif escolha == 3:
        if valor_um > valor_dois:
            print(f'{valor_um} eh maior que {valor_dois}.\n')
        elif valor_um == valor_dois:
            print(f'{valor_um} eh igual a {valor_dois}.\n')
        else:
            print(f'{valor_dois} Eh maior que {valor_um}.\n')

    elif escolha == 4:
        print('Todos os valores[1] ou apenas um[2] ?\n')
        escolha_um = int(input('Sua escolha:\n'))

        if escolha_um == 1:
            valor_um = int(input('Digite um novo valor para 1:\n'))
            valor_dois = int(input('Digite um novo valor para 2:\n'))
            ficha = 5
        elif escolha_um == 2:
            print('Qual dos dois valores Você quer alterar ? [1,2]\n')
            escolha_dois = int(input('Digite seu valor.\n'))

            if escolha_dois == 1:
                valor_um = int(input('Digite um novo valor para 1:\n'))
                ficha = 5
            elif escolha_dois == 2:
                valor_dois = int(input('Digite um novo valor par 2:\n'))
                ficha = 5
            else:
                print('Valor incorreto, tente Novamente.')
                ficha = 5
        else:
            print('Valor invalido. Tente Novamente')
            ficha = 5
    elif escolha == 5:
        print('Programa encerrado com Sucesso.\nTenha um Bom Dia :)')
        ficha = 0