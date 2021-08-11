# Frase que vai aparecer em um arquivo Txt existente
frase = "Digite sua frase aqui:\nDê um trocado pro seu bruxo."

# Nome do Arquivo - "a" para escrever no arquivo
with open("Caminho Do Seu Arquivo", "a") as file:
    file.write(frase)


