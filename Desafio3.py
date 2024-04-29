import re

def validade_numero_telefone(phone_number):
    pattern = re.complie('[(])[0-9]{2}[)]][\n][0-9]')
    if re.match(pattern, phone_number):
        return f'Numero de telefone valido'
    else:
        return f'Numero invalido'
    
phone_number = input()
result = validade_numero_telefone(phone_number)
print(result)

#Deu certo aqui, vejamos no treco da Dio
# e la deu erro, wonderfull