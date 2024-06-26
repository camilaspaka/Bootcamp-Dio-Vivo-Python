#[].append

lista = []
lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])
    
print(lista)

#[].copy

l2 = lista.copy()
print(lista)
print(id(l2), id(lista))

l2[0] = 2

print(l2)
print(lista)

#[].count

cores = ["Vermelho", "Azul", "Amarela", "Verde", "Roxo", "Preto", "Cinza", "Lilás", "Rosa", "Magenta", "Vermelho"]

print(cores.count("Vermelho"))
print(cores.count("Azul"))
print(cores.count("Magenta"))

#[].extend
linguagens = ["python", "js", "go"]

print(linguagens)

linguagens.extend(["java", "csharp"])

print(linguagens)

#[].index

linguagens =["python", "js", "c", "java", "csharp"]

print(linguagens.index("java"))
print(linguagens.index("python"))

#[].pop

linguagens =["python", "js", "c", "java", "csharp"]
print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop(0))

#[].remove

linguagens =["python", "js", "c", "java", "csharp"]
linguagens.remove("c")
print(linguagens)

#[].reverse

linguagens =["python", "js", "c", "java", "csharp"]
linguagens.reverse()
print(linguagens)

#[].sort

linguagens = ["python", "js", "c", "java", "csharp"]
print(linguagens.sort())

linguagens = ["python", "js", "c", "java", "csharp"]
print(linguagens.sort(reverse=True))

linguagens = ["python", "js", "c", "java", "csharp"]
print(linguagens.sort(key=lambda x: len(x)))

linguagens = ["python", "js", "c", "java", "csharp"]
print(linguagens.sort(key=lambda x: len(x), reverse=True))

#len

linguagens =["python", "js", "c", "java", "csharp"]
print(len(linguagens))

#[].sorted

linguagens =["python", "js", "c", "java", "csharp"]
print(sorted(linguagens, key=lambda x: len(x)))

print(sorted(linguagens, key=lambda x: len(x), reverse=True))

#[].clear

lista.clear()
print(lista)

