frutas = ["laranja", "maca", "uva", "manga", "pera", "morango"]
print(frutas[-4])

frutas1 = []
print(frutas1)

letras = list("python")
print(letras)

numero1 = list(range(10))
print(numero1)

carro = ["Ferrari", "F8", 4200000, 2024, 2900, "São Paulo", True]
print(carro)

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]
print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

lista = ["p", "y", "t", "h", "o", "n"]
print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])
print(lista[::-1])

carros = ["gol", "celta", "kicks", "palio", "sandero", "ferrari"]
for carro in carros:
    print(carro)

carros = ["gol", "celta", "kicks", "palio", "sandero", "ferrari"]
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")


numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
quadraro = []

for numero in numeros:
    if numero % 2 == 0:
        print(pares)
for numero in numeros:
    print(quadraro.append(numero ** 2))
