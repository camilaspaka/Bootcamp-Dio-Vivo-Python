class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade

p = Pessoa("Camila", 29)
print(p.nome, p.idade)