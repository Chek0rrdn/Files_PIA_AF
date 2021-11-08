# SCRIPT CREADO PARA ORGANIZAR LOS ARCHIVOS RECUPERADOS POR LA HERRAMIENTA DE RECUPERACION #
import pathlib

def main():

    # ruta = pathlib.Path('.')
    ruta = pathlib.Path('/mnt/d/Documents/RAW/recuperados/recup_dir.2/')

    diccionario = {k : [v for v in ruta.glob(f'*{k}')]
        for k in {archivo.suffix for archivo in ruta.iterdir()}
    }

    for extension, archivos in diccionario.items():
        
        carpeta = ruta / extension[1:]
        carpeta.mkdir()

        for archivo in archivos:
            archivo.replace(carpeta / archivo.name)


if __name__ == '__main__':
	main()