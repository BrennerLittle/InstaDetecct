
import os
import shutil
blacklist = ["Blittlle_followers.txt","loadnames.py","main.py","known_faces","unknown_faces"]
dirs = os.listdir()
for x in blacklist:
    dirs.remove(x)
print(dirs)
for item in dirs:
    shutil.move(item,"known_faces")


