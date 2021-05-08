nota_um = float(input('Digite sua primeira nota: '))
nota_dois = float(input('Digite sua segunda nota: '))

media = (nota_um + nota_dois)/2

if media == 7 or media > 7:
    print('Aprovado')
elif media < 5.0:
    print('Reprovado')
elif media == 5.0 or media < 6.9:
    print('Recuperação')

print(f'Sua média foi: {media}')