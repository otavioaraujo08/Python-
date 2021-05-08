produto = 100
desconto_vc = (produto * 10)/100
desconto_av = (produto * 5)/100
juros = (produto * 20)/100

print(f'O produto custou R${produto} Reais.')
print('Escolha uma forma de pagamento:\n1: A vista ou cheque.\n2: Cartão.')
escolha = int(input('Qual a sua escolha ?\n'))

if escolha == 1:
    print(f'O valor com desconto de R${desconto_vc} reais, sai por R${produto - desconto_vc} Reais.')
elif escolha == 2:
    print('1:A vista ou 2: Parcelado')
    escolha_um = int(input('Qual a sua escolha ?\n'))
    if escolha_um == 1:
        print(f'O valor com desconto de R${desconto_av} reais, fica em R${produto - desconto_av} Reais.')
    elif escolha_um == 2:
        print('Quanta vezes ?')
        escolha_dois = int(input('Eu escolho:\n'))
        if escolha_dois == 2:
            print(f'Preço: {produto}')
        elif escolha_dois == 3 or escolha_dois > 3:
            print(f'O valor com desconto de {juros} fica em: R${produto - juros} Reais.')
        else:
            print('ERROOOOOU')
else:
    print('Valor incorreto')
print('\nBela compra.')