'''
Created on 09.10.2022

@author: vital
'''
with open(r'C:\Users\vital\git\transformers\examples\pytorch\language-modeling\Dialoge.txt',encoding='UTF8') as f:
    with open(r'C:\Users\vital\git\transformers\examples\pytorch\language-modeling\DialogeLines.txt',  mode="w", encoding="utf-8") as w:
        sentences = f.read().split(".")
        for sentence in sentences: 
            w.write(sentence+"\n")