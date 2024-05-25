def somar(a, b):
    return a + b

def subtrair(a, b):
    return a- b

def test(a, b):
    return a*2 + b*4

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é igual a {a} + {b} = {resultado}")

exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtrair)
exibir_resultado(10, 10, test)

op = somar
print(op(1, 23))