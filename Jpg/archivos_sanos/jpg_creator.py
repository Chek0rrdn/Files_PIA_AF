#CREAR 50 IMAGENES#
import os, random
import shutil

def main():
    ruta = "/home/edgar/Dev/Files_PIA_AF/Jpg/archivos_sanos"
    archivos = os.listdir(ruta)
    
    for i in range(1, 60):    
        imagen_seleccionado = random.choice(archivos)
        shutil.copy2(imagen_seleccionado, f'imagen_seleccionado_{i}.jpg')

if __name__ == '__main__':
	main()