# Ocorre Qunando Uma Classe Filha Recebe A Herança De Outra Classe Filha
class Organismo:
    # Caso Esteja Vivo
    vivo = True


class Animal(Organismo):
    # Função Indicando Do Que Os Animais Se Alimentam
    def comer(self):
        print("O Animal Está Se Alimentando.")


class Cachorro(Animal):
    # Função Indicando Como O Animal Se Comunica
    def falar(self):
        print("O Cachorro Se Comunica Por Latidos.")


# Chamando A Classe
cachorro = Cachorro()

# Mostrando Os Dados
print(f'O Animal Está Vivo ?\n{cachorro.vivo}')
print(f"Como Ele Se Alimenta ?")
cachorro.comer()
print(f"Como Ele Se Comunica ?")
cachorro.falar()