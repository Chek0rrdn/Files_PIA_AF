#CREAR 10 ARCHIVOS POWER POINT#
import random
from pptx import Presentation
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches

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

    for iteracion in range(1, 11):
        # Creación del documento
        ppt = Presentation()

        #Añadimos una Slide (Presentacio)
        title_slide_layout = ppt.slide_layouts[0]
        slide = ppt.slides.add_slide(title_slide_layout)
        title = slide.shapes.title
        subtitle = slide.placeholders[1]

        title.text = "Análisis Forénse!"
        subtitle.text = "presentacion "+str(iteracion)+" hecha en Python!"


        #Agregamos una nueva slide para el Grafico
        slide = ppt.slides.add_slide(ppt.slide_layouts[6]) 


        #Añadimos un Gráfico
        chart_data = CategoryChartData()  
        
        chart_data.categories = ['East', 'West', 'Midwest', 'Northeast']   
        
        chart_data.add_series('Series 1',  
                            (23,35,20,29))
        
        x, y, cx, cy = Inches(2), Inches(2), Inches(6), Inches(4.5)  
        
        slide.shapes.add_chart( XL_CHART_TYPE.COLUMN_CLUSTERED, x, 
                            y, cx, cy, chart_data ) 



        #Añadimos un Slide para l a Forma
        slide = ppt.slides.add_slide(ppt.slide_layouts[9])
        shapes = slide.shapes


        shapes.title.text = 'Agregando una Forma'

        left = Inches(0.93)  # 0.93" centra este conjunto general de formas
        top = Inches(3.0)
        width = Inches(1.75)
        height = Inches(1.0)

        shape = shapes.add_shape(MSO_SHAPE.PENTAGON, left, top, width, height)
        shape.text = 'Paso 1'

        left = left + width - Inches(0.4)
        width = Inches(2.0)  # los galones necesitan más ancho para el equilibrio visual

        for n in range(2, 6):
            shape = shapes.add_shape(MSO_SHAPE.CHEVRON, left, top, width, height)
            shape.text = 'Paso %d' % n
            left = left + width - Inches(0.4)


        #Añadimos un Slide para una tabla
        title_only_slide_layout = ppt.slide_layouts[10]
        slide = ppt.slides.add_slide(title_only_slide_layout)
        shapes = slide.shapes

        shapes.title.text = 'Agregando una Tabla'

        rows = cols = 2
        left = top = Inches(2.0)
        width = Inches(6.0)
        height = Inches(0.8)

        table = shapes.add_table(rows, cols, left, top, width, height).table

        # establecer anchos de columna
        table.columns[0].width = Inches(2.0)
        table.columns[1].width = Inches(4.0)

        # escribir encabezados de columna
        table.cell(0, 0).text = 'Foo'
        table.cell(0, 1).text = 'Bar'

        # escribir datos de las celdas
        table.cell(1, 0).text = 'Baz'
        table.cell(1, 1).text = 'Qux'

        #Guardamos la Presentación
        titulo_presentacion = elegir_materia()
        titulo_presentacion = titulo_presentacion+str(iteracion)+".pptx"
        
        ppt.save(titulo_presentacion) 
        


if __name__ == '__main__':
	main()
print("Hecho!!!")