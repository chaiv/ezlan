'''
Created on 20.11.2022

@author: vital
'''

import os
import shutil
lJDatasetID = "LJ001"
importpath =  r"G:\Meine Ablage\ezlan\recordings"
exportpath =   r"G:\Meine Ablage\ezlan\ttsdata\wavs"
l=os.listdir(importpath)
for file in l:
    filename = file.split('.')[0]
    shutil.copy(importpath+"/"+file, exportpath+"/"+lJDatasetID+"-"+filename.zfill(4)+".wav")
        

