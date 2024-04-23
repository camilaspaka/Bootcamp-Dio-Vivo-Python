numeros = set([1, 2, 3, 4, 5, 4, 6, 7, 8, 9, 2, 8, 9, 2, 3,])
numero = list(numeros)
fruta = set("abacaxi")
carros = set(("palio", "celta", "palio", "uno", "up"))
print(numeros)
print(fruta)
print(carros)
linguagues = ("python", "java", "go", "r", "python", "js")
print(linguagues)

#{}.union

conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a.union(conjunto_b)

#{}.intersection
conjunto_a = {11, 10, 9}
conjunto_b = {12, 13, 14}

conjunto_a.intersection(conjunto_b)

#{}.difference
conjunto_a = {11, 10, 9}
conjunto_b = {12, 13, 14}

conjunto_a.difference(conjunto_b)
conjunto_b.difference(conjunto_a)

#{}.symetric_difference
conjunto_a = {11, 10, 9}
conjunto_b = {12, 13, 14}

conjunto_a.symmetric_difference(conjunto_b)

#{}.issubset
conjunto_a = {11, 10, 9}
conjunto_b = {12, 13, 14}
conjunto_a.issubset(conjunto_b)
conjunto_b.issubset(conjunto_a)

#{}.issuperset
conjunto_a = {11, 10, 9}
conjunto_b = {12, 13, 14}
conjunto_a.issuperset(conjunto_b)
conjunto_a.issuperset(conjunto_a)

#{}.isdisjoint
conjunto_a = {11, 10, 9}
conjunto_b = {12, 13, 14}
conjunto_c = {15, 16}
conjunto_a.isdisjoint(conjunto_b)
conjunto_a.isdisjoint(conjunto_c)

#{}.add
sorteio = {1, 23}
sorteio.add(25)
sorteio.add(40)
sorteio.add(5)

#{}.clear

sorteio = {1, 23}
print(sorteio)
sorteio.clear
print(sorteio)

#{}.copy
sorteio = {1, 23}
print(sorteio)
sorteio.copy
print(sorteio)

#{}.discard
numeros = {1, 2, 3, 4, 5, 4, 6, 7, 8, 9, 2, 8, 9, 2, 3,}
print(numeros)
numeros.discard(1)
numeros.discard(9)
print(numeros)

#{}.pop
numeros = {1, 2, 3, 4, 5, 4, 6, 7, 8, 9, 2, 8, 9, 2, 3,}
print(numeros)
numeros.pop()
numeros.pop()
print(numeros)

#{}.remove

#{}.len

#{}.in