#CREAR 25 ARCHIVOS EXCEL#
import openpyxl
import random

nombres = (
    "RecetaPaciente_","RecetaLab._","Nota_",
    "HistoriaClinica_","ResumenDeCaso_","Pedidos_",
    "ListaMedica_","Medicamentos_","Antibioticos_",
    "FormatoHist.Clinica_","ListaEstServicioSoc","Estudiantes_",
    "ListEnfermeras_","Nomina_","Presupuestos_",
    "ListadoHerramientas_","ListaInstrumentos_","PedidosMeds_",
    "PedidosMateriales_","Materiales_"
)

contraseñas = (
    '*%3a@&6y27bZ', 
    'K5%i!85$@6iD',
    '!4iY*7L3@7^6',
    'v965H5DQ%$&*',
    'X9*4$G%7@k2^',
    '@b89%@QT4v4^',
    'Ys&59@@GQ9%8',
    '*5e85#aV3#*r',
    '7$#V7b^8#Ae5',
    '9X*kX*364e%#'
)

nombres_ex = (
    'edgar','juan','alberto','alicia','pedro','alejandro','martin'
)

def elegir_materia():
    materia = random.choice(nombres)
    materia.encode()
    return materia

def main():
    for iteracion in range(1, 26):

        referencias = ['a859', 'b125', 'c764', 'd399', 'User', 'Pass']
        precios = [9.95, 4.95, 19.95, 49.95, random.choice(nombres_ex).encode(), random.choice(contraseñas).encode()]
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