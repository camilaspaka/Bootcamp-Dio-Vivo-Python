from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2024-05-22 14:10"
mascar_ptbr = "%d/%m/%Y %a"
mascara_en = "%Y/%m/%d, %H:%M"

print(data_hora_atual.strftime(mascar_ptbr))

data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)
print(type(data_convertida))