p_a = int(input('Digite o primeiro termo:\n'))
razao = int(input('Digite a razão:\n'))

for c in range(0,10):
    print(f'P.A: {p_a} RAZÃO: {razao}.')
    p_a += razao
    print(f'P.T: {p_a}')