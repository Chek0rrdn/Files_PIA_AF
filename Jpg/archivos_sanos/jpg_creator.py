#CREAR 50 IMAGENES#
import os
import pathlib
import random
import shutil

CURRENT_DIR = pathlib.Path().resolve()

def main():

    if not CURRENT_DIR.joinpath("imagenes").exists():
        CURRENT_DIR.joinpath("imagenes").mkdir()

    if not CURRENT_DIR.joinpath("imagenes", "imagenes_2").exists():
        CURRENT_DIR.joinpath("imagenes_2").mkdir()

    archivos = os.listdir(CURRENT_DIR.joinpath("imagenes"))
    
    for i in range(1, 51):    
        imagen_seleccionado = random.choice(archivos)
        shutil.copy2(CURRENT_DIR.joinpath("imagenes", f"{imagen_seleccionado}"), CURRENT_DIR.joinpath("imagenes_2",f"img_{i}.jpg"))

if __name__ == '__main__':
	main()
