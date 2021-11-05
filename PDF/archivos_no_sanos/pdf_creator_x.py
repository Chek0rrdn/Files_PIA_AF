#CREAR 10 ARCHIVOS PDF#
import itertools, random
from random import randint
from statistics import mean
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


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
        def grouper(iterable, n):
            args = [iter(iterable)] * n
            return itertools.zip_longest(*args)


        def export_to_pdf(data):

            titulo_pdf = elegir_materia()
            titulo_pdf = titulo_pdf+str(iteracion)+".pdf"

            c = canvas.Canvas(titulo_pdf, pagesize=A4)
            w,h = A4
            max_rows_per_page = 45
            # Margenes.
            x_offset = 50
            y_offset = 50
            # espacio entre rows.
            padding = 15
            
            xlist = [x + x_offset for x in [0, 200, 250, 300, 350, 400, 480]]
            ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
            
            for rows in grouper(data, max_rows_per_page):
                rows = tuple(filter(bool, rows))
                c.grid(xlist, ylist[:len(rows) + 1])
                for y, row in zip(ylist[:-1], rows):
                    for x, cell in zip(xlist, row):
                        c.drawString(x + 2, y - padding + 3, str(cell))
                c.showPage()
            
            c.save()


        data = [("NOMBRE", "NOTA 1", "NOTA 2", "NOTA 3", "PROM.", "ESTADO")]

        for i in range(1, 101):
            exams = [randint(0, 10) for _ in range(3)]
            avg = round(mean(exams), 2)
            state = "Aprobado" if avg >= 4 else "Desaprobado"
            data.append((f"Alumno {i}", *exams, avg, state))
        
        export_to_pdf(data)


if __name__ == '__main__':
	main()
print("Hecho!!!")