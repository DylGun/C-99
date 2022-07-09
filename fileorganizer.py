from importlib.metadata import files
from importlib.resources import path
import os
import shutil
from unicodedata import name
path=input("Enter the folder to be sorted: ")
listoffiles=os.listdir(path)
for file in listoffiles:
    name,ext=os.path.splitext(file)
    ext=ext[1:]
    if ext=='':
        continue
    if os.path.exists(path+'/'+ext): 
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file) 
        
    else: 
        os.makedirs(path+'/'+ext) 
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)