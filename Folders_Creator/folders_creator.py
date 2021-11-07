#CREAR 30 CARPETAS Y 10 OCULTAS
import os, random

materias = (
    'POO',
    'Labs_POO',
    'Telecomunicaciones1',
    'Telecomunicaciones2',
    'Telecomunicaciones3',
    'Telecomunicaciones4',
    'lab_Tele3',
    'lab_Tele4',
    'lab_Tele1',
    'lab_Tele2',
    'Programacion1',
    'Lab_Progra1',
    'IngenierriaaSocial',
    'SistemasOperativaos',
    'SeguridadDesarrolloSsoftware',
    'SegBasesDatos',
    'BasesDatos',
    'LabBD',
    'SEGA',
    'LabSEGA',
    'Coco',
    'Criptografia',
    'DiseñoArquitecturas',
    'NTSI',
    'SegCompNube',
    'CompForenseAbogados',
    'DiseOrientadoObjetos',
    'labDOO',
    'TopicosTecnologias1',
    'TopicosTecnologias2'
)


def main():
    
    for i in materias:
        os.mkdir(f'./carpetas/{i}')

    f = open('chanchuyo.txt', 'w')

    contador = 0
    while contador < 10:
        carp_oculta = random.choice(materias)

        try:
            if os.path.isdir(f'./carpetas/{carp_oculta}/.top_secret'):
                print(f'la carpteta {carp_oculta}/.top_secret YA existe')
            else:
                os.mkdir(f'./carpetas/{carp_oculta}/.top_secret')
                f.write(f'La carpeta Oculta se guardo en {carp_oculta}\n')
                contador += 1

        except ValueError as ve:
            print(ve)        
    
    f.close()


if __name__ == '__main__':
	main()
print("Hecho!!!")