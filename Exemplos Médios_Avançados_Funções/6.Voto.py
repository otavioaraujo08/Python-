from datetime import date


def voto(nasc):
    atual = date.today().year
    idade = atual - nasc

    print(f'A sua idade eh:{idade}')
    if idade > 17:
        print('Você é maior de idade, portanto deve votar obrigatoriamente.')
    elif idade == 17:
        print('Você tem idade para votar, porém ainda não é Obrigatório.')
    else:
        print('Você é menor de idade, ainda não possui idade para votar.')


idade = int(input(f'Digite o seu ano de nascimento:\n'))
voto(idade)