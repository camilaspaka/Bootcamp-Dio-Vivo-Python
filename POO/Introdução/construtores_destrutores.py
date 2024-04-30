class Cachorro:
    def _init_(self, nome, cor, acordado=True):
        print("Inicializando")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def _del_(self):
        print("Removendo a classe")

    def falar(self):
        print("auau")

def criar_cachorro():
    c = Cachorro("Pitty", "caramelo", False)
    print(c)