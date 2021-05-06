salario = float(input('Qual o valor do seu salário ?\n'))
aumento_um = (salario * 10)/100
aumento_dois = (salario * 15)/100

print(f'Salário anterior: R$ {salario}. NOVO SALÁRIO: {salario + aumento_um}'
      if salario >= 1250
      else f'Salário anterior: R$ {salario}. NOVO SALÁRIO: {salario + aumento_dois}')