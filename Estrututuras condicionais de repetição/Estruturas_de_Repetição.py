#Exemplo sem repetição

a = int(input("Informe um número inteiro: "))
print(a)

a += 1
print(a)

a += 1

print(a)

#Com repetição



#for /else
texto = input("Informe um texto: ")
Vogais = "AEIOU"

for letra in texto:
    if letra.upper() in Vogais:
        print(letra, end="")
else:
    print()
    print("Isso é o que sobra")

#range

for numero in range(0, 11):
    print(numero, end=" ")

for numero in range(0, 51, 5):
    print(numero, end=" ")
