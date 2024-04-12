#Exemplo 

saldo = 1000
saque = 200
limite = 100

saldo >= saque

saque <= limite

#Operador E

saldo = 1000
saque = 200
limite = 100
saldo >= saque and saque <= limite

#Operador OU
saldo = 100
saque = 200
limite = 100

saldo >= saque or saque <= limite

#Operador Negação 

contatos_emergencia = []

not 1000 > 1500

not contatos_emergencia

not "saque 1500;"

not " "

#Parênteses

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque

print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

print(exp_2)

#Testes

print(True and True and True)
print(True and False and True)
print(False and False and False)
print(True or True or True)
print(True or False or False)
print(False or False or False)

saldo_suficiente = (saldo >= saque and saque <= limite)
conta_especial_com_saldo = conta_especial and saldo >= saque 