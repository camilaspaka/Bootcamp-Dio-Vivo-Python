try:
    with open('examplee.txt', 'r', enconding='utf-8') as arquivo:
         print('trabalhando no arquivo')
except IOError as exc:
     print("Erro ao abrir o arquivo {exc}")