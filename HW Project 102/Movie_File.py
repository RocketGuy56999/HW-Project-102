import os
import shutil
from_dir="./Source_Folder/"
to_dir="./Final_Folder/"
list_of_files = os.listdir(from_dir)
print(list_of_files)

for fileName in list_of_files:
    name,extension=os.path.splitext(fileName)
    if extension=="":
        continue
    if extension in[".gif",".png", ".jpg",".docx"]:
        path1=from_dir+'/'+fileName
        path2=to_dir+'/'+"ImageFiles"
        path3=to_dir+'/'+"ImageFiles"+'/'+fileName
        
        if os.path.exists(path2):
            shutil.move(path1,path2)

        else:
            os.makedirs(path2)
            shutil.move(path1,path2)