#CREAR 10 IMAGENES#
import os, random
import shutil

def main():

    archivos = os.listdir('./imagenes')
    
    for i in range(1, 11):    
        imagen_seleccionado = random.choice(archivos)
        shutil.copy2(f'./imagenes/{imagen_seleccionado}', f'imagen_seleccionado_{i}.png')

if __name__ == '__main__':
	main()