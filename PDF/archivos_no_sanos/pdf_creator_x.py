#CREAR 10 ARCHIVOS PDF#
import os, random
from docx2pdf import convert


def main():

    for i in range(1,11):

        archivos = os.listdir('./archivos_base')

        word_seleccionado = random.choice(archivos)

        inputFile = f'./archivos_base/{word_seleccionado}'
        outputFile = f'{word_seleccionado}.pdf'
        file = open(outputFile, "w")
        file.close()

        convert(inputFile, outputFile)


if __name__ == '__main__':
	main()
print("Hecho!!!")