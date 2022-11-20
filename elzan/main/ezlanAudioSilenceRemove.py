'''
Created on 18.10.2022

@author: vital
'''
import os
from pydub.silence import split_on_silence
from pydub import AudioSegment

def cut_silence(importpath, exportpath):
    audio_format = "wav"
    # Reading and splitting the audio file into chunks
    sound = AudioSegment.from_file(importpath, format = audio_format) 
    audio_chunks = split_on_silence(sound
                            ,min_silence_len = 100
                            ,silence_thresh = -65
                            ,keep_silence = 50
                        )

    # Putting the file back together
    combined = AudioSegment.empty()
    for chunk in audio_chunks:
        combined += chunk
    combined.export(exportpath, format = audio_format)
    

importpath =  r"G:\Meine Ablage\ezlan\recordings"
exportpath =   r"G:\Meine Ablage\ezlan\ttsdata\wavs"
l=os.listdir(importpath)
for file in l: 
    cut_silence(importpath+"/"+file, exportpath+"/"+file)


    


        

        
        
