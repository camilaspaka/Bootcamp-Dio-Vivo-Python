def dizer_oi(nome):
    return f"Oi {nome}"

def incentivar_aprender(nome):
    return f"Oi {nome}, vamos aprender Python! "

def mensagem_para_usuario(funcao_mensagem):
    return funcao_mensagem("Usuario")

mensagem_para_usuario(dizer_oi)
mensagem_para_usuario(incentivar_aprender)