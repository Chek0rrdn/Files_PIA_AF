#CREAR 10 IMAGENES#
import shutil
from PIL import Image


def main():

    im = Image.open('archivo.PNG')
    imagen = im.convert('RGB')
    imagen.save('imagenjotapege.jpg', quality=95)

    for iterador in range(1, 11):
        shutil.copy2('imagenjotapege.jpg', f'imagenjotapege_{iterador}.jpg')

if __name__ == '__main__':
	main()