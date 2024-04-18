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

#Exemplo 

maior_idade = 18

idade = int(input("Informe sua idade: "))
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

#Exemplo If/Elif e Else
conta_normal = 2000000
conta_universitaria = 50000
saque = 5000
saldo = 2000000
cheque_especial = 50000000000
if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com cheque especial")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque autorizado")
    else:
        print("Saque não autorizado")