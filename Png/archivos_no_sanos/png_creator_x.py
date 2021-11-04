#CREAR 10 IMAGENES#
import shutil

def main():

    for iterador in range(1, 11):
        shutil.copy2('imagenpenege.PNG', f'imagenpenege_{iterador}.PNG')

if __name__ == '__main__':
	main()