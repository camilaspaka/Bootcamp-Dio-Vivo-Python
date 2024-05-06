class Estudante:
    escola = "Dio"

    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
    
    def __str__(self):
        return f"{self.nome} ({self.numero}) - {self.escola}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)
    
cah = Estudante("Camila", 24951)
mah = Estudante("Marilia", 47859)

mostrar_valores(cah, mah)
