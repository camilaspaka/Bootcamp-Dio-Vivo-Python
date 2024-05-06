class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade
    
    @classmethod
    def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

p = Pessoa("Camila", 29)
print(p.nome, p.idade)

p1 = Pessoa().criar_apartir_data_nascimento(1995, 2, 6, "Camila")
print(p1.nome, p1.idade)