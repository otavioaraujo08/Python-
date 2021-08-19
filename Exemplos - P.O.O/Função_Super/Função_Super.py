# Função Super: é usado para dar acesso as classes parentes,
#               retornando objetos temporários as classes parentes.

class Retangulo:
    # Método Construtor
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura


class Quadrado(Retangulo):
    # Método Construtor
    def __init__(self, altura, largura):
        super().__init__(altura, largura)

    def area(self):
        # Multiplicando Os Valores De Altura E Largura
        return self.altura * self.largura


class Cubo(Retangulo):
    # Método Construtor
    def __init__(self, altura, largura, comprimento):
        super().__init__(altura, largura)
        self.comprimento = comprimento

    # Herdando Os Valores de Self
    def volume(self):
        # Multiplicando O Volume Do Cubo
        return self.altura * self.altura * self.comprimento


quadrado = Quadrado(2, 2)
cubo = Cubo(3, 2, 4)

print("A Área do Quadrado é:")
print(quadrado.area())

print("O Vólume Do Cubo é:")
print(cubo.volume())
