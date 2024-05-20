def dizer_oi(nome):
    print('executando nome')
    return f"Oi {nome}"

def incentivar_aprender(nome):
    print('executando incentivar aprender')
    return f"Oi {nome}, vamos aprender Python! "

def executar(funcao):
    print('executando executar')
    return funcao('Camila')

print(executar(dizer_oi))