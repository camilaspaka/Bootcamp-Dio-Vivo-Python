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