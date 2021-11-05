#CREAR 50 CANCIONES MP3#
import random
import shutil

nombres_Canciones = (
    'Shepherd_of_Fire',
    'Hail_to_the_King',
    'Doing_Time',
    'This_Means_War',
    'Requiem',
    'Crimson_Day',
    'Heretic',
    'Coming_Home',
    'Planets',
    'Acid_Rain',
    'This_Means_War'
)

def elegir_cancion():
    cancion = random.choice(nombres_Canciones)
    cancion.encode()
    return cancion


def main():
    
    for i in range(1, 51):    
        cancion_seleccionada = elegir_cancion()
        shutil.copy2(f'./cancion/Carry_On.mp3', f'{cancion_seleccionada}_{i}.mp3')

if __name__ == '__main__':
	main()