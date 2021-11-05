#CREAR 25 ARCHIVOS EXCEL#
import openpyxl
import random

nombres = (
    'Final_Poo_tarea_',
    'Labs_POO_tarea_',
    'Telecomunicaciones1_tarea_',
    'Telecomunicaiones2_tarea_',
    'lab_Tele3_tarea_',
    'lab_tele4_tarea_',
    'Programacion1_tarea_',
    'IngenierriaaSocial_tarea_',
    'SistemasOperativaos_tarea_',
    'SDS_tarea_',
    'segBasesDatos_tarea_',
    'BasesDatos_tarea_',
    'SEGA_tarea_',
    'LabSEGA_tarea_',
    'Coco_tarea_',
    'Criptografia_tarea_',
    'DiseñoArquitecturas_tarea_',
    'NTSI_tarea_',
    'SegCompNube_tarea_'
)

def elegir_materia():
    materia = random.choice(nombres)
    materia.encode()
    return materia

def main():
    for iteracion in range(1, 26):

        referencias = ['a859', 'b125', 'c764', 'd399', 'User', 'Pass']
        precios = [9.95, 4.95, 19.95, 49.95, 'edgar', 'Eq++4gdWjm^s2b$>']
        productos = []

        for i in range(1,400):
            random.shuffle(referencias)
            random.shuffle(precios)
            productos.append(('producto_'+str(i), referencias[0], 1500, precios[0]))
            productos.append(('producto_'+str(i+1), referencias[1], 600, precios[1]))
            productos.append(('producto_'+str(i+2), referencias[2], 200, precios[2]))
            productos.append(('producto_'+str(i+3), referencias[3], 2000, precios[3]))
            productos.append(('producto_'+str(i+4), referencias[4], 0, precios[4]))
            productos.append(('producto_'+str(i+5), referencias[5], 0, precios[5]))

        wb = openpyxl.Workbook()
        hoja = wb.active

        # Crea la fila del encabezado con los títulos
        hoja.append(('Nombre', 'Referencia', 'Stock', 'Precio', 'Otros'))

        for producto in productos:
            # producto es una tupla con los valores de un producto 
            hoja.append(producto)


        titulo_documento = elegir_materia()
        titulo_documento = titulo_documento + str(iteracion)+".xlsx"

        wb.save(titulo_documento)


if __name__ == '__main__':
	main()
print("Hecho!!!")