#CREAR 20 ARCHIVOS OGG#
import os, random
import shutil

def main():

    archivos = os.listdir('./ogg_base')

    for i in range(1, 21):
        nombre_seleccionado = random.choice(archivos)
        shutil.copy2(f'./ogg_base/{nombre_seleccionado}',f'{nombre_seleccionado}_{i}.ogg')


if __name__ == '__main__':
	main()