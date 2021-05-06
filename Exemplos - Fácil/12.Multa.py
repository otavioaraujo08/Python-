velocidade = float(input('Qual a sua velocidade ?\n'))
multa = velocidade % 80

print(f'Você foi multado: (.\nO valor da sua multa eh: {(multa*7):.1f}'
      if velocidade > 80.0 else 'Exercício 29: Você não foi multado :).')