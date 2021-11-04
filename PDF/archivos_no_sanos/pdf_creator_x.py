#CREAR 10 ARCHIVOS PDF#
import itertools
from random import randint
from statistics import mean
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def main():
    for iteracion in range(1, 11):
        def grouper(iterable, n):
            args = [iter(iterable)] * n
            return itertools.zip_longest(*args)


        def export_to_pdf(data):

            titulo_pdf = "pidiefAFFcFm_"+str(iteracion)+".pdf"
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