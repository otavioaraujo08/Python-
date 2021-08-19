# A Classe Carro Vai Ser Importada ao arquivo index("From_Import")
class Carro:

    # Método Chamado Para iniciar uma classe e permitir que ela seja inicializada
    def __init__(self, marca, modelo, ano, cor):
        # Informações Para Construção De Um Carro Para Ser Informado Depois
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    # Caso esteja tudo Correto
    def dirigir(self):
        print(f"O Carro {self.marca} Está Funcionando")

    # Caso Não esteja funcionando
    def parar(self):
        print(f"O Carro {self.marca} Está Parado")
