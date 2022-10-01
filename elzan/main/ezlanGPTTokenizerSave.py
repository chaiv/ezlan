'''
Created on 01.10.2022

@author: vital
'''
from transformers import GPT2Tokenizer


t = GPT2Tokenizer.from_pretrained(r'C:\tmp\ezlanByteTokenizer')
print(t.encode("Wim Dehnke"))
#t.save_pretrained(r'C:\tmp\ezlanByteTokenizer')