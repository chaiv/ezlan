'''
Created on 25.09.2022

@author: vital
'''
from nltk.corpus import stopwords


german_stop_words = stopwords.words('german')

dialogeLines = open(r'C:\Users\vital\git\transformers\examples\pytorch\language-modeling\DialogeLinesWithoutStopwords.txt',  mode="x")

def stop_word_removal(x):
    token = x.split()
    return ' '.join([w for w in token if not w in german_stop_words])

with open(r'C:\Users\vital\git\transformers\examples\pytorch\language-modeling\DialogeLines.txt',  mode="r", encoding="utf-8") as f:
    for row in f.readlines(): 
        dialogeLines.write(stop_word_removal(row)+"\n")
    