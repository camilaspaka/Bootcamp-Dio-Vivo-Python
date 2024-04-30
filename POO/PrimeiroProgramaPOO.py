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

    #def _str_(self):
     #   return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"

    def _str_(self):
        return f"{self.__class__.__name__}: {','.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta()
b1.buzinar()
b1.correr()
b1.parar()
b1.cor()
b1.modelo()
b1.ano()
b1.valor()