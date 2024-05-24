try:
    with open('examplee.txt', 'r') as arquivo:
         print('trabalhando no arquivo')
except IOError as exc:
     print("Erro ao abrir o arquivo {exc}")