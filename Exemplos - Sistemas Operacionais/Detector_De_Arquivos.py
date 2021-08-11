# Importação da biblioteca para o sistema interno do Windows
import os

# Inserindo o local a ser descoberto
path = "Caminho Do Seu Arquivo"

# Comparado pra saber se é um caminho Válido
if os.path.exists(path):
    print("É um caminho válido, portanto verdadeiro!")
    # Comparando para verificar se é um ARQUIVO
    if os.path.isfile(path):
        print("\nÉ um arquivo real !")
    # Caso for um PASTA
    elif os.path.isdir(path):
        print("\nÉ um Diretório real !")
else:
    print("Caminho invalido!")
