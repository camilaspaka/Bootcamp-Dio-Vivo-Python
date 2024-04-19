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

#range built-in

for zero in range(0, 11):
    print(zero, end=" ")

print()

for numero in range(0, 51, 5):
    print(numero, end=" ")
    print()

#while

opcao = -1
while opcao != 0:
    opcao = int(input("[1]Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigada e até a proxima!!!")

#break

opcao = -1
while opcao != 0:
    opcao = int(input("Informe um numero: "))

    if opcao == 10:
        break

    print(opcao)

#True

while True:
    numero = int(input("Informe um numero: "))

    if numero == 10:
        break

    print(numero)

#breank and continue

for valor in range(100):
    if valor % 2 == 0:
        continue
    print(valor, end=" ")