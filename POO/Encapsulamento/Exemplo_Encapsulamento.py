class Conta:
    def _init_(self, saldo=0):
        self.saldo = saldo
        
    def depositar(self, valor):
        pass
    def sacar(self,valor):
        pass

conta = Conta(100)
print(conta.saldo)