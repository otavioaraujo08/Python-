par_impar = int(input('Digite um valor:\n'))
conta = par_impar % 2

print(f' Valor: {par_impar} eh Par' if conta == 0
      else f'Valor {par_impar} eh impar')