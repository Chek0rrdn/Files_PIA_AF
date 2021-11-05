import os
import subprocess
import shutil

for fn in os.listdir('.'):
    if os.path.isfile(fn):
        if fn.endswith(".mp4"):
            print("mp4 file found: " + fn)
            p = subprocess.run(
                ["ffmpeg",
                "-i", fn,
                "-n",
                "-acodec", "copy",
                "-vcodec", "copy",
                "-f", "mov", fn[:-4] + ".mov"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=False)
            if p.returncode == 0:

                print("Convertido " + fn)

                for i in range(1,51):
                    shutil.copy('./video.mov', f'./video_mov_{i}.mov')
                
                os.remove(fn)
                
            else:
                print("Skipped   " + fn)

