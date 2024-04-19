#Exemplo sem repetição

a = int(input("Informe um número inteiro: "))
print(a)

a += 1
print(a)

a += 1

print(a)

#Com repetição



#for  
texto = input("Informe um texto: ")
Vogais = "AEIOU"

for letra in texto:
    if letra.upper() in Vogais:
        print(letra, end="")
print()