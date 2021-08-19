class Animal:
    # Caso Ele Esteja Vivo
    vivo = True

    # Do Que Ele Se Alimenta
    def eat(self):
        print("O animal está se alimentado.")

    # Como Ele Dorme
    def sleep(self):
        print("O animal está dormindo")


# Herdará as características de "Animal"
class Coelho(Animal):
    def correr(self):
        print("O Coelho Está Correndo A 45 Mph")


class Aguia(Animal):
    def voar(self):
        print("A Águia Está Voando Na Velocidade de 320 KM/H")


class Tubarao(Animal):
    def nadar(self):
        print("O Tubarão Está Nadando A 56 KM/H")


# Variáveis que armazenam as classes
coelho = Coelho()
aguia = Aguia()
tubarao = Tubarao()

# Executando algumas classes
aguia.eat()
tubarao.sleep()
