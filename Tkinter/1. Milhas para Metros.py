# -x-x-x-x- CONFIGURAÇÕES DE PROGRAMA -x-x-x-x-
from tkinter import *
from tkinter import ttk


# Função para Calcular Milhas -> Metros
def calcular(*args):
    try:
        valor = float(milhas.get())
        metros.set(int(0.3048 * valor * 10000 + 0.5) / 10000.0)
    except ValueError:
        pass


# Declarando a minha tela
tela = Tk()
# Nome do meu Programa
tela.title("Milhas para Metros")

# Estilização da Tela
tela_principal = ttk.Frame(tela, padding="3 3 12 12")
tela_principal.grid(column=0, row=0, sticky=(N, W, E, S))
tela.columnconfigure(0, weight=1)
tela.rowconfigure(0, weight=1)

# Declarando nossa variável e configurando para aceitar vários tipos de valores(Objeto, Valor, String)
milhas = StringVar()
# Configurando para exibir na tela principal e gravar o valor na variável "milhas"
milhas_iniciais = ttk.Entry(tela_principal, width=7, textvariable=milhas)
milhas_iniciais.grid(column=2, row=1, sticky=(W, E))

# Declarando nossa variável e configurando para aceitar vários tipos de valores(Objeto, Valor, String)
metros = StringVar()
# Configurando para exibir na tela principal e gravar o valor na variável "metros"
ttk.Label(tela_principal, textvariable=metros).grid(column=2, row=2, sticky=(W, E))

# Criando um boão para realizar o calculo
ttk.Button(tela_principal, text="Calcular", command=calcular).grid(column=3, row=3, sticky=W)

# Adicionando textos na tela para direcionar o usuário
ttk.Label(tela_principal, text="Milhas").grid(column=1, row=1, sticky=W)
ttk.Label(tela_principal, text="Metros").grid(column=1, row=2, sticky=W)

# Caso seja necessário um espaço
for child in tela_principal.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Dando enfase à variável "Milhas_iniciais"
milhas_iniciais.focus()

# Gerando o retorno de nossa função "Calcular"
tela.bind("<Return>", calcular)

# Executando O Programa
tela.mainloop()
