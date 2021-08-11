# Frase que vai aparecer em um arquivo Txt existente
frase = "Digite sua frase aqui:\nDê um trocado pro seu bruxo."

# Nome do Arquivo - "w" para rescrever no arquivo
with open("Caminho Do Seu Arquivo", "w") as file:
    file.write(frase)