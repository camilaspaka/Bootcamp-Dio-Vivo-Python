def dizer_oi(nome):
    return f"Oi {nome}"

def incentivar_aprender(nome):
    return f"Oi {nome}, vamos aprender Python! "

def mensagem_para_camila(funcao_mensagem):
    return funcao_mensagem("Camila")

mensagem_para_camila(dizer_oi)
mensagem_para_camila(incentivar_aprender)