total = mais_mil = mais_caro = cont = 0
caro = ''

while True:
    nome = input('Qual o nome do seu produto ?\n')
    preco = float(input('Digite o preço do seu produto:\n'))
    total += preco
    cont += 1

    if cont == 1 or preco < preco:
        mais_caro = preco
        caro = nome
    if preco > 1000:
            mais_mil += 1

    print('Quer continuar ? [S,N]')
    escolha = input('').upper()

    if escolha == 'N':
        break
print(f'Valor total: {total}\nProdutos mais caros que R$ 1000: {mais_mil}.'
      f'\nProduto mais caro: R${mais_caro} e seu nome: {caro}.')
