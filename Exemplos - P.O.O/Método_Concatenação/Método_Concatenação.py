# Método De Concatenação Consiste Em Chamar Vários Métodos Sequencialmente.
class Carro:

    def ligar(self):
        print("Você Deu Partida No Carro !")
        return self

    def dirigir(self):
        print("Você Está Dirigindo O Carro !")
        return self

    def freio(self):
        print("Você Apertou O Freio !")
        return self

    def desligar(self):
        print("Você Desligou O Carro !")
        return self


carro = Carro()

# Concatenando Várias Funções Em Uma Só Ligação
carro.ligar()\
    .dirigir()\
    .freio()\
    .desligar()
