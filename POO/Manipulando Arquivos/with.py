try:
    with open('example.txt', 'r') as arquivo:
         print('trabalhando no arquivo')
except IOError:
     print("Erro ao abrir o arquivo")