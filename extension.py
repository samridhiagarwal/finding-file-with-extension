#project to extract all the files of certain extension from your computer and dump them in another folder.


import os
import fnmatch
import glob
import shutil
path = "C:\Users\Public\pytho\pyco"
l = []
flag = 0
source_dir = "C:\Users\Public\pytho\pyco"
dest_dir = "C:\Users\Public\pytho\destin"
s = input("Enter the extension to be moved in the format (*.extension): ")
for root, dirs, files in os.walk(path):
    for _file in files:
        if fnmatch.fnmatch(_file,s):
            l.append(os.path.join(root,_file))
            flag = 1 
            files = glob.iglob(os.path.join(source_dir,s))
            #for file in files:
                #if os.path.isfile(file):
                    #shutil.copy(file, dest_dir)
if flag == 0 :
     print ("No Element Found")
else:
    for i in range (len(l)):
        print (i+1 , '.\t', l[i], '\n')
        shutil.copy(l[i], dest_dir)
