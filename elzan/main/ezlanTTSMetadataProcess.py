#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
Created on 29.10.2022

@author: vital
'''
delimiter = "|"
startNumber = 1
maxSentences = 433
lJDatasetID = "LJ001"
crlf = "\n" 
spcial_char_map = {ord('ä'):'ae', ord('ü'):'ue', ord('ö'):'oe', ord('ß'):'ss',ord('Ä'):'Ae', ord('Ü'):'Ue', ord('Ö'):'Oe'}
with open(r'G:\Meine Ablage\ezlan\DialogeLines.txt',encoding='UTF8') as f:
    with open(r'G:\Meine Ablage\ezlan\ttsdata\metadata.csv',  mode="w", encoding="cp1252") as w:
        sentences = f.readlines()
        for sentenceIndex in range(startNumber,maxSentences+1): 
            sentenceProcessed =  sentences[sentenceIndex].rstrip(crlf)
            sentenceProcessed =  sentenceProcessed.translate(spcial_char_map)
            w.write(lJDatasetID+"-"+str(sentenceIndex).zfill(4)+delimiter+  sentenceProcessed+delimiter+  sentenceProcessed+'\n')