numero = int(input('Escolha um valor:\n'))
escolha = int(input('Escolha uma base de conversão entre 1 e 3:\n'
                    '1 Para binário.\n2 Para octal.\n3 Para hexadecimal.\n'))

if escolha == 1:
    print(f'Binário: {bin(numero)[2:]}')
elif escolha == 2:
    print(f'Octal: {oct(numero)[2:]}')
elif escolha == 3:
    print(f'Hexadecimal: {hex(numero)[2:]}')
else:
    print('Valor não encontrado, tente novamente.')