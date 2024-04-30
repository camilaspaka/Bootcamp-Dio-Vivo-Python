class Bicicleta:
    def _init_(self, cor ,modelo ,ano ,valor):
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

b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()

