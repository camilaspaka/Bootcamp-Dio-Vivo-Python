class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade
    
    @classmethod
    def criar_apartir_data_nascimento(self, ano, mes, dia, nome):
        idade = 2024 - ano
        return Pessoa(nome, idade)

p = Pessoa("Camila", 29)
print(p.nome, p.idade)

p1 = Pessoa().criar_apartir_data_nascimento(1995, 2, 6, "Camila")
print(p1.nome, p1.idade)