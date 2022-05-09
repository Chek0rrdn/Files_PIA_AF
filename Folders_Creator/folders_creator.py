#CREAR 30 CARPETAS Y 10 OCULTAS
import os
import pathlib
import random

CURRENT_DIR = pathlib.Path().resolve()

materias = (
    "Antibioticos","Estudiantes","FormatoHist.Clinica","Formatos","HistoriasClinicas",
    "Hists.Clinicas","Hospitales","Instrumentales","ListadoHerramientas","ListaEstServicioSoc",
    "ListaFormatos","ListaMedica","ListaMedicamentos","ListasInstrumentos","ListEnfermeras",
    "Materiales","Medicamentos","Meds","Nominas","Pedidos",
    "PedidosDeMateriales","PedidosMateriales","PedidosMedicamentos","PedidosMedicos","PedidosMeds",
    "Presupuesto","Presupuestos","ResumensDeCasos","TurnosEnfermeros","TurnosMeds",
)


def main():
    
    if not CURRENT_DIR.joinpath("carpetas").exists():
        CURRENT_DIR.joinpath("carpetas").mkdir()

    for i in materias:
        os.mkdir(CURRENT_DIR.joinpath("carpetas", f"{i}"))

    f = open('chanchuyo.txt', 'w')

    contador = 0
    while contador < 10:
        carp_oculta = random.choice(materias)

        try:
            if os.path.isdir(CURRENT_DIR.joinpath("carpetas", f"{carp_oculta}", ".top_secret")):
                print(f"la carpteta {carp_oculta}/.top_secret YA existe")
            else:
                os.mkdir(CURRENT_DIR.joinpath("carpetas", f"{carp_oculta}", ".top_secret"))
                f.write(f"La carpeta Oculta se guardo en {carp_oculta}\n")
                contador += 1

        except ValueError as ve:
            print(ve)   
    
    f.close()


if __name__ == '__main__':
	main()
print("Hecho!!!")
