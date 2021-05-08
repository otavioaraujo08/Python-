peso = float(input('Qual o seu peso ?'))
altura = float(input('Qual a sua altura ?'))

imc = peso/(altura * altura)

if imc < 18.5:
    print('\nAbaixo do peso')
elif imc == 18.5 or imc < 25:
    print('\nPeso ideal')
elif imc == 25 or imc < 30:
    print('\nSobrepeso')
elif imc == 30 or imc < 40:
    print('\nObesidade ')
else:
    print('\nObesidade Morbida')

print('\nSeu I.M.C eh : {}'.format(imc))