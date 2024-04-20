#Exemplo IF

saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Sacado!")
if saldo < saque:
    print("Sem dindin")

#Novo exemplo Else

saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Sacado!")
else: 
    print("Sem dindin")

#Exemplo Elif

opcao = int(input("Informe uma opção : [1]Sacar \n [2]Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para saque: "))

elif opcao == 2:
    print("Exibindo o extrato...")
else:
    sys.exit("Opção invalidade")

#Exemplo 2

maior_idade = 18

idade = int(input("Informe sua idade: "))
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

