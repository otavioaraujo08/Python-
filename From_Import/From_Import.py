# Realizando a Importação Da Classe Carro
from Carro import Carro

carro_um = Carro("Chevrolet", "Esportivo", 2021, "Preto")

print(f"O Carro: {carro_um.marca}\nModelo: {carro_um.modelo}.\nAno: {carro_um.ano}.\nCor: {carro_um.cor}")
print(carro_um.dirigir())
