class Cachorro:
    def _init_(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    def latir(self):
        print ("Auau")
    def dormir(self):
        self.acordado = False
        print("Zzzzz")
        