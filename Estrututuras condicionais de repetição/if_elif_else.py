conta_normal = 20000
conta_universitaria = 5000
saque = 5000
saldo = 2000
cheque_especial = 500
if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com cheque especial")
    else:
        print("Saque não autorizado")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque autorizado")
    else:
        print("Saque não autorizado")