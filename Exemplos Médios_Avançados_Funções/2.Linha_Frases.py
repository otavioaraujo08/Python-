

def escrever(valor, frase):
    print('-' * valor)
    print(frase)
    print('-' * valor)


texto = input('Digite seu textão aqui:\n')
val = len(texto)

escrever(val, texto)