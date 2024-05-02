class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando motor")

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    pass

moto = Motocicleta("preta", "abc-1234", 2)
print(moto)
moto.ligar_motor()

carro = Carro("branco", "xde-0000", 4)
carro.ligar_motor()

caminhao = Caminhao("roxo","fgd-8787", 8)
caminhao.ligar_motor()

