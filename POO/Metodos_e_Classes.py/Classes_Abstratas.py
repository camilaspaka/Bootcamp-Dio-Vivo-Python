from abc import ABC

class ControleRemoto(ABC):
    def ligar(self):
        pass

    def desligar(self):
        pass

class ControleTV:
    pass

controle = ControleTV()
controle.ligar()
controle.desligar()
