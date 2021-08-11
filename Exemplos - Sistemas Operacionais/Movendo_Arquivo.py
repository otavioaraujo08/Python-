# Biblioteca "OS" para pegar os diretórios do sistema
import os

# Arquivo que ira ser movido - Destino que ira ter o arquivo
arquivo = "Teste.txt"
destino = "C:\\Users\\josil\\Desktop\\Teste.txt"

# Tentativa para verificar se o arquivo foi encontrado e caso houver sucesso em mover-lo
try:
    if os.path.exists(destino):
        print("O Arquivo encontrou seu destino")
    else:
        os.replace(arquivo, destino)
        print(f'{arquivo} foi movido com Sucesso !')
except FileNotFoundError:
    print("O arquivo não foi encontrado :C")
