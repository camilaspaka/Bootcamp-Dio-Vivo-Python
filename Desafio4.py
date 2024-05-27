class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.__nome = nome
        self.__numero = numero
        self.__plano = plano
    
    def __str__(self):
        return f"Usuário {self.__nome} criado com sucesso."


# Entrada:
nome = input()
numero = input()
plano = input()


# Criação do objeto UsuarioTelefone
usuario = UsuarioTelefone(nome, numero, plano)


# Saída:
print(usuario)