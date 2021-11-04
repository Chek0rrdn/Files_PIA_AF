#CREAR 10 videos#
from moviepy.editor import *


def main():
    for iterador in range(1, 11):
        
        video = VideoFileClip("video.mp4")
        cortado = video.subclip(iterador+1, 30)

        nombre_video_coratdo = "video_cortado"+str(iterador)+".mp4" 
        cortado.write_videofile(nombre_video_coratdo)


if __name__ == '__main__':
	main()
print("Hecho!!!")