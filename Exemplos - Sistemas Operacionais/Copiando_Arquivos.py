# Biblioteca "Shutil" encarregada de realizar essa função
import shutil

# Nome do usuário para imersão :D
nome = input("Digite o seu nome !\n")

# Usuário escolhe o que deseja ser retornado
print(f"Seja bem a copiadora do sr@ {nome}.\nO que você deseja ?")
print("1: Copiar os dados de um arquivo.\n2:Copiar um arquivo para outro local.\n3:Copiar Arquivo + Pasta.")

while True:
    escolha = int(input("Faça sua escolha:\n"))

    if escolha == 1:
        # Aqui o usuário precisa digitar o nome do arquivo e seu destino
        shutil.copyfile("Nome Arquivo", "Destino")
        print("Trabalho Concluido, Tenha Um Bom Dia :D")
        break
    elif escolha == 2:
        # Aqui o usuário precisa digitar o nome do arquivo e seu destino
        shutil.copy("Nome Arquivo", "Destino")
        print("Trabalho Concluido, Tenha Um Bom Dia :D")
        break
    elif escolha == 3:
        # Aqui o usuário precisa digitar o nome do arquivo e seu destino
        shutil.copy2("Nome Arquivo", "Destino")
        print("Trabalho Concluido, Tenha Um Bom Dia :D")
        break
    else:
        print("Valor invalido, digite apenas o que está escrito :P")
