valor = input('Digite um valor a ser provado: ')

print('True = Verdadeiro.\nFalse = Falso.')
print(f'\nÉ um valor númerico ? -x-{valor.isnumeric()}-x-\n'
      f'É uma letra ? -x- {valor.isalpha()} -x-\n'
      f'É um letra maiuscula ? -x- {valor.isupper()} -x-')

