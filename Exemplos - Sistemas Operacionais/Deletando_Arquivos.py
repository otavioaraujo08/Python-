# Biblioteca "OS" para pegar os diretórios do sistema
import os

# Módulo "Remove" da biblioteca "OS" para apagar arquivos.
os.remove("Seu caminho")

'''
Outra forma:
# Caminho Do Arquivo
caminho = "exemplo.txt"

# Tente Realizar
try:
    os.rmdir(caminho)
# Caso Não Encontre O Arquivo
except FileNotFoundError:
    print("Arquivo Não Encontrado")
# Caso não tenha permissão
except PermissionError:
    print("Você Não Tem Permissão Para Remover Esse Arquivo !")
else:
    print(f"{caminho} Foi Removido Com Sucesso !")
'''
