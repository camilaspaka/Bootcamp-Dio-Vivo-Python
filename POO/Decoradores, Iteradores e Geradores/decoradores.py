def dizer_oi(nome):
    print('executando nome')
    return f"Oi {nome}"

def incentivar_aprender(nome):
    print('executando incentivar aprender')
    return f"Oi {nome}, vamos aprender Python! "

def mensagem_para_camila(funcao_mensagem):
    return funcao_mensagem("Camila")

def executar(funcao):
    print('executando executar')
    return funcao()

executar(mensagem_para_camila(dizer_oi))
executar(mensagem_para_camila(incentivar_aprender))