# Nesse Método Prevalece A Classe Que For Chamada
class Animal:
    def comer(self):
        print("O Animal Está Se Alimentando")


class Coelho(Animal):
    # Do Que O Coelho Se Alimenta !
    def comer(self):
        print("O Coelho Se Alimenta De Cenoura")


# Instanciando A Classe Em Uma Variável
coelho = Coelho()

# Chamando A Classe
print("Do Que O Coelho Se Alimenta ?")
coelho.comer()
