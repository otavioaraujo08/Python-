# Aqui instanciamos Classes que funcionarão como objetos de outras classes
class Supermercado:
    nome: None
    local: None


# Adicionando os Objetos da Classe "Supermercado"
def alterar_nome(supermercado, nome):
    supermercado.nome = nome


# Adicionando os Objetos da Classe "Supermercado"
def alterar_local(supermercado, local):
    supermercado.local = local


# Instanciando Classes
supermercado_um = Supermercado()
supermercado_dois = Supermercado()
supermercado_tres = Supermercado()

# Alterando o valor delas
print("\nQual é o nome do primeiro Supermercado e sua Localização ?")
alterar_nome(supermercado_um, "Lider")
alterar_local(supermercado_um, "Rua dos Pariquis.")
print(f"Nome: {supermercado_um.nome}\nLocal: {supermercado_um.local}")

print("\nQual é o nome do segundo Supermercado e sua Localização ?")
alterar_nome(supermercado_dois, "Magazine Luiza")
alterar_local(supermercado_dois, "Rua Quinze de Novembro")
print(f"Nome: {supermercado_dois.nome}\nLocal: {supermercado_dois.local}")

print("\nQual é o nome do terceiro Supermercado e sua Localização ?")
alterar_nome(supermercado_tres, "Americanas")
alterar_local(supermercado_tres, "Rua Batista Campos")
print(f"Nome: {supermercado_tres.nome}\nLocal: {supermercado_tres.local}")
