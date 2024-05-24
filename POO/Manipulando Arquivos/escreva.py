file = open('example.txt', 'w')
file.write("Ola Camila.")
file.writelines(["\n", "Escrevendo ", "um ", "novo ", "texto ", "para ", "mostrar ", "o ", "writelines!"])
file.close()