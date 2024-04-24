frutas = ("laranja", "pera", "uva", "melancia", "manga",)
print(frutas[-2])

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",)
print(pais)

matriz = (
    (1, "a", 2),
    ("b", 3, 5),
    (6, 5, "c"),
)

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-2])
print(matriz[-1][-3])

tupla = ("p", "y", "t", "h", "o", "n",)

print(tupla[2:])
print(tupla[:2])
print(tupla[1:3])
print(tupla[0:3:2])
print(tupla[::])
print(tupla[::-1])

carros = ("gol", "celta", "kicks", "up", "palio", "sandero")
for carro in carros:
    print(carro)
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

#().count

cores = ("vermelho", "roxo", "azul", "verde", "preto", "verde", "roxo", "verde")

print(cores.count("verde"))
print(cores.count("roxo"))
print(cores.count("preto"))

#().index

linguagens = ("python", "java", "c", "js", "go",)
print(linguagens.index("java"))
print(linguagens.index("python"))

#len

linguagens = ("python", "java", "c", "js", "go",)
print(linguagens)