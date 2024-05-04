class Estudante:
    escola = "Dio"

    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
    
    def __str__(self):
        return f"{self.nome} ({self.numero}) - {self.escola}"
    
cah = Estudante("Camila", 24951)
mah = Estudante("Marilia", 47859)