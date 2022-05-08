#CREAR 100 ARCHIVOS EXCEL#
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

def elegir_materia():
    materia = random.choice(nombres)
    materia.encode()
    return materia

def main():
    for iteracion in range(1, 101):

        referencias = ['a859', 'b125', 'c764', 'd399']
        precios = [9.95, 4.95, 19.95, 49.95]
        productos = []

        for i in range(1,400):
            random.shuffle(referencias)
            random.shuffle(precios)
            productos.append(('producto_'+str(i), referencias[0], 1500, precios[0]))
            productos.append(('producto_'+str(i+1), referencias[1], 600, precios[1]))
            productos.append(('producto_'+str(i+2), referencias[2], 200, precios[2]))
            productos.append(('producto_'+str(i+3), referencias[3], 2000, precios[3]))


        wb = openpyxl.Workbook()
        hoja = wb.active

        # Crea la fila del encabezado con los títulos
        hoja.append(('Nombre', 'Referencia', 'Stock', 'Precio'))

        for producto in productos:
            # producto es una tupla con los valores de un producto 
            hoja.append(producto)


        titulo_documento = elegir_materia()
        titulo_documento = titulo_documento + str(iteracion)+".xlsx"

        wb.save(titulo_documento)


if __name__ == '__main__':
	main()
print("Hecho!!!")