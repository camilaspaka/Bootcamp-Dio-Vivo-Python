import re

def validate_numero_telefone(phone_number):
    pattern = r"\(\d{2}\) 9\d{4}-\d{4}"
    if re.match(pattern, phone_number):
        return f'Número de telefone valido'
    else:
        return f'Número de telefone invalido'
    
phone_number = input()

result = validate_numero_telefone(phone_number)
print(result)

#Deu certo aqui, vejamos no treco da Dio
# e la deu erro, wonderfull
#esqueci de copiar e colar o código direito kkkk genio
#não to sabendo dizer onde é o erro, ahhhhhhhhhhhhhhhh
