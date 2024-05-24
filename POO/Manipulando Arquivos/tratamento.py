try:
    file = open('non_existent_file.txt', 'r')
except FileNotFoundError:
    print("Arquivo não encontrado") 