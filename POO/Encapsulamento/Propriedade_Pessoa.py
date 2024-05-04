class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self.ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self.name
    
    @property
    def idade(self):
        _ano_atual = 2022
        return _ano_atual - self._ano_nascimento
    
pessoa = Pessoa("Camila", 1995)
print(f"Nome: {pessoa.nome} \t Idade: {pessoa.idade}")
