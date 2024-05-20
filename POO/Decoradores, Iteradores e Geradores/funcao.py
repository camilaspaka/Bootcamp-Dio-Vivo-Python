def calcular(operacao):
    def somar(a, b):
        return a + b
    
    def subtrair(a, b):
        return a - b
    
    if operacao == "+":
        return somar
    else:
        return subtrair
    
resultado = calcular("+")(1, 3)
print(resultado)