def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = input(msg)
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'Digite um número inteiro valido.')
        if ok:
            break
    return valor


val = leiaInt('Digite um valor:\n')
print(f'Voce acabou de digitar o valor: {val}')