import os
import shutil

#cria diretorio
os.mkdir("old.txt")
#renomeia arquivo
os.rename("old.txt", "new.txt")
#remove arquivo
os.remove("unwanted.txt")
#move arquivo
shutil.move("source.txt", "destination.txt")
