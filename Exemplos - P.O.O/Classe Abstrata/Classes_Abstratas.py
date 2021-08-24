# Impede que o usuário de criar um objeto dessa classe,
# obrigando um usuário de sobreescrever uma classe filha

# Necessário fazer o import da biblioteca ABC do método ABC e abstractmethod
from abc import ABC, abstractmethod


# Classe Abstrata -> Uma Classe que contém um ou mais métodos abstratos
class Veiculo(ABC):
    # Método Abstrato -> Um método que possui declarações que não necessitam ser implementadas.
    @abstractmethod
    def rodas(self):
        pass

    @abstractmethod
    def lugares(self):
        pass


class Carro(Veiculo):

    def rodas(self):
        print("Um carro normalmente possui quatro rodas XD !")

    def lugares(self):
        print("Dependendo do carro, ele possui cinco lugares !")


class Moto(Veiculo):

    def rodas(self):
        print("Uma moto normalmente possui duas rodas :D !")

    def lugares(self):
        print("Dependendo da moto, ela possui dois lugares !")


# Instanciando as Classes
carro = Carro()
moto = Moto()

# Chamando as classes
print("Quantas rodas um carro possui ?\nQuantos lugares também ?")
carro.rodas()
carro.lugares()
print("\nQuantos lugares uma moto possui ?\nE quantas rodas ?")
moto.lugares()
moto.rodas()
