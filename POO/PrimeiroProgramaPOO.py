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

    def _str_(self):
        return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"

