def calcular(operacao):
    def somar(a, b):
        return a + b
    
    def subtrair(a, b):
        return a - b
    
    match operacao:
        case "+":
            return somar
        case "-":
            return subtrair
        
resultado = calcular("+")(1, 3)
print(resultado)