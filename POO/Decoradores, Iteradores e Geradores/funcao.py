def calcular(operacao):
    def somar(a, b):
        return a + b
    
    def subtrair(a, b):
        return a - b
    
    def multiplicar(a, b):
            return a * b
    
    def dividir(a, b):
            return a / b
    
    match operacao:
        case "+":
            return somar
        case "-":
            return subtrair
        case "*":
            return multiplicar
        case "/":
            return dividir
        
op = calcular("+")
print(op(180, 90))
op = calcular("-")
print(op(180, 90))
op = calcular("*")
print(op(180, 90))
op = calcular("/")
print(op(180, 90))