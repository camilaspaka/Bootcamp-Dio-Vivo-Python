import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent
#os.mkdir(ROOT_PATH / "novo-diretorio")

arquivo = open("novo.txt", "w")
arquivo.close()