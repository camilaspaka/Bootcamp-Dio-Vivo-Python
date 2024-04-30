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

    def cor(self):
        print("Vermelho")

    def modelo(self):
        print("desconhecido")

    def ano(self):
        print("2022")

    def valor(self):
        print("660")

b1 = Bicicleta()
b1.buzinar()
b1.correr()
b1.parar()
b1.cor()
b1.modelo()
b1.ano()
b1.valor()