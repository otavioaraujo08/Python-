# Várias Heranças Em Uma Mesma Classe Filha
class Presa:
    # Como Ela Vai Fugir ?
    def fugir(self):
        print("O Animal É Uma Presa !")


class Predador:
    # Como Ele Vai Caçar ?
    def predar(self):
        print("O Animal É Um Predador !")


class Cobra(Presa, Predador):
    # A Cobra É Presa Da Águia
    def veneno(self):
        print("A Cobra Mata A Vítima Por Veneno !")

    def serpentina(self):
        print("A Cobra Se Locomove Dos Predadores Por Serpentina !")


class Aguia(Predador):
    # A Águia É Predador Da Cobra
    def bicar(self):
        print("A Águia Caça Sua Vitimas Através De Mordidas e Bicadas")


class Rato(Presa):
    # O Rato É Predaro Da Águia E Da Cobra
    def correr(self):
        print("O Rato Foge Dos Predarores Correndo E Se Escondendo")

# Inserindo As Classes Em Variáveis
cobra = Cobra()
aguia = Aguia()
rato = Rato()


print("Como O Rato Foge De Seus Predadores ?")
rato.fugir()
rato.correr()

print("\nComo A Cobra Foge E Ataca ?")
cobra.predar()
cobra.fugir()
cobra.veneno()


print("\nComo A Águia Caça Suas Vítimas ?")
aguia.predar()
aguia.bicar()
