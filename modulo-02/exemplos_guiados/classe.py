class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.km = 0

    def rodar(self, distancia):
        self.km += distancia

    def painel(self):
        return f"{self.modelo}: {self.km} km"

meu = Carro("Fiat", "fusca")
outro = Carro("VW", "Gol")
print(meu.marca, meu.modelo, meu.km)
print(outro.modelo)
print(type(meu).__name__)

meu.rodar(120)
meu.rodar(30)
print(meu.painel())