import random

cpu = random.randint(0,10)
focus = tentativas = 0

while focus == 0:
    escolha = int(input('Tente adivinhar a mão da cpu:\n'))
    if escolha == cpu:
        print('Você acertou.')
        focus = 1
    else:
        print('Valor incorreto. Tente novamente :( \n')
        tentativas += 1
print(f'\nA MÁQUINA ESCOLHEU {cpu}.\nVOCÊ DEMOROU {tentativas} ESCOLHAS PARA ACERTAR')
