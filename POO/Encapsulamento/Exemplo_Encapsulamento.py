class Conta:
    def _init_(self, nro_agencia , saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self,valor):
        self._saldo -= valor

    def mostar_saldo(self):
        return self._saldo

conta = Conta()
conta.depositar(100)
print(conta.nro_agencia)
print(conta._saldo)