#CREAR 10 IMAGENES#
import os, random
import shutil

def main():
    ruta = "./imagenes_base/"
    archivos = os.listdir(ruta)
    
    for i in range(1, 21):    
        imagen_seleccionado = random.choice(archivos)
        shutil.copy2(f'./imagenes_base/{imagen_seleccionado}', f'imagen_seleccionado_{i}.jpg')

if __name__ == '__main__':
	main()