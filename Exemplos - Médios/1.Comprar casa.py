valor_da_casa = float(input('Qual o valor da casa ?\n'))
salario = float(input('Quanto você recebe ?\n'))
qnts_anos = int(input('Quantos anos você vai pagar isso ?\n'))

prestacao = valor_da_casa / qnts_anos

print(f'Valor da casa: {valor_da_casa}.'
      f'\nSalário do meliante: {salario}.'
      f'\nQuanto anos pretende pagar: {qnts_anos}')

if prestacao < (0.3 * salario):
    print('\033[4;32;40mCompra Aprovada\33[m')
else:
    print('\033[4;31;40mCompra rejeitada: Trabalhe mais.\33[m')
print('\nValor da prestação: {}.'.format(prestacao))