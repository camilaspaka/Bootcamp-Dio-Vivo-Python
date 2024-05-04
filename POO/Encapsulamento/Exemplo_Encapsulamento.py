class Conta:
    def _init_(self, saldo=0):
        self.saldo = saldo
        
    def depositar(self, valor):
        self._saldo += valor

    def sacar(self,valor):
        self._saldo -= valor

conta = Conta(100)
conta.depositar(100)
print(conta._saldo)