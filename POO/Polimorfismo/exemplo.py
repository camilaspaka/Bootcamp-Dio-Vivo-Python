class Passaro:
    def voar(self):pass

class Pardal(Passaro):
    def voar(self):
        print("Pardal Voa")

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")

def plano_de_voo(obj):
    obj.voar()

plano_de_voo(Pardal())
plano_de_voo(Avestruz())
p1 = Pardal()
p2 = Avestruz()
