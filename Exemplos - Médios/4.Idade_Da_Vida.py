idade = int(input('Digite seu ano de nascimento:\n'))
idade_cal = 2021 - idade

if idade_cal < 9 or idade_cal == 9:
    print('Você é alguém na idade Mirim')
elif idade_cal < 9 or idade_cal == 14:
    print('Você é alguém na idade Infantil')
elif idade_cal < 14 or idade_cal == 19:
    print('Você é alguém na idade junior')
elif idade_cal == 20:
    print('Você é alguém na idade Senior')
else:
    print('Você é alguém na idade Master')

print('Sua idade eh: {}'.format(idade_cal))