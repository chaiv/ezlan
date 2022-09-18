'''
Created on 11.09.2022

@author: vital
'''
from transformers import pipeline

pipe = pipeline('text-generation', model=r'C:\tmp\ezlan-gpt',
                 tokenizer=r'C:\tmp\ezlan-gpt')

text = pipe("Kennst du Wim Dehnke?", max_length=100)[0]["generated_text"]

print(text)