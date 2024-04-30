class Bicicleta:
    def _init_(self, cor,modelo ,ano ,valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Pipipi")

    def parar(self):
        print("Parando...")
        print("Bicicleta parada")

    def correr(self):
        print("vrumvrum")

b1 = Bicicleta()
b1.buzinar()
b1.correr()
b1.parar()

