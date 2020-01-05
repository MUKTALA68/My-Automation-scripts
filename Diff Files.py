import os
import shutil

os.chdir('C:\\')  # Make sure you add your source and destination path below

dir_src =("\\ajeshwil-w7\\TestFiles\\Customer Files & Xfe_7.1.3")
dir_dst =("\\baent\\UserSharing\SendMe\\PrintMe\\Customer Files\\XF Team")

for filename in os.listdir(dir_src):
    if filename.endswith('.txt'):
        shutil.copy(dir_src + filename, dir_dst)
    print(filename)
