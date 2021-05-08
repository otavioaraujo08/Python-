frase = input('Digite sua frase:\n').strip().upper()
palavra = frase.split()

junto = ''.join(palavra)
print(junto)

inverso = junto[::-1]

if inverso == junto:
    print('Temos um palíndromo')
else:
    print('Não temos um palindro')

print(f'NORMAL: {junto}.\nINVERSO: {inverso}.')