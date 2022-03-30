import os
cwd = os.getcwd() # get current working directory
print(cwd)

#os.mkdir("new_directory")#create new folder in current directory

#os.makedirs("new_direct1/new2") # create nested folder in current directory

#os.rmdir("new_directory")

# os.rmdir("new_direct1")

dirs = os.listdir()

for dir in dirs:
    if dir.endswith('.py'):
        print(dir)
from datetime import *
metadata = os.stat("FileHand_1.py")
print("metadata =",metadata)
print(datetime.fromtimestamp(metadata.st_atime))
print(datetime.fromtimestamp(metadata.st_mtime))
print("size =",metadata.st_size)