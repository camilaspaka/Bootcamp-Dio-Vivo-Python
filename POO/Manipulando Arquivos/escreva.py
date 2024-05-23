file = open('example.txt', 'w')
file.write("Ola Camila")
file.writelines([". Escrevendo ", "um ", "novo ", "texto ", "para ", "mostrar ", "o ", "writelines!"])
file.close()