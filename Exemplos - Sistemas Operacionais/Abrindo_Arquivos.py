# Aqui vai haver uma Tentativa de executar um arquivo
try:
    # Após o "open" você coloca o caminho do seu arquivo
    with open("Caminho do Seu Arquivo") as file:
        print(file.read())
        print("Arquivo Lido Com Sucesso !")
# Caso ele não encontre
except FileNotFoundError:
    print("Arquivo não encontrado !")
