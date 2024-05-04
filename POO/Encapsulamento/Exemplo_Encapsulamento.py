class Conta:
    def _init_(self, nro_agencia , saldo=0):
        self.saldo = saldo
        self.nro_agencia = nro_agencia
        
    def depositar(self, valor):
        self._saldo += valor

    def sacar(self,valor):
        self._saldo -= valor

conta = Conta(100)
conta.depositar(100)
print(conta._saldo)