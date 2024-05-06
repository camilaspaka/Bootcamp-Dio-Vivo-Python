from abc import ABC

class ControleRemoto(ABC):
    def ligar(self):
        pass

    def desligar(self):
        pass

class ControleTV:
    def ligar(self):
        print("Ligando")
        print("Tv ligada")
    def desligar(self):
        print("Desligando a TV")
        print("Desligou")

controle = ControleTV()
controle.ligar()
controle.desligar()
