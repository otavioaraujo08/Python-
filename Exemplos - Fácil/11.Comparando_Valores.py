valor_um = int(input('Dgite um valor para 1:\n'))
valor_dois = int(input('Dgite um valor para 2:\n'))
valor_tres = int(input('Dgite um valor para 3:\n'))

if valor_um > valor_dois and valor_um > valor_tres:
    print(f' O maior valor entre os 3 eh: {valor_um}.')
elif valor_dois > valor_um and valor_dois > valor_tres:
    print(f'O maior valor entre os 3 eh: {valor_dois}.')
elif valor_tres > valor_um and valor_tres > valor_dois:
    print(f'O maior valor entre os 3 eh: {valor_tres}.')
elif valor_tres == valor_um and valor_tres == valor_dois:
    print(f'Os três possuem valores iguais.')