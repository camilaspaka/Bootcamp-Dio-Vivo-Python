class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def _iter_(self):
        return self
    
    def _next_(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration
    
for i in MeuIterador(numeros=[1, 2, 3]):
    print(i)