'''
Created on 30.09.2022

@author: vital
'''
from tokenizers import ByteLevelBPETokenizer

tokenizer = ByteLevelBPETokenizer()

tokenizer.train(files=r'G:\Meine Ablage\Dialoge.txt', vocab_size=52_000, min_frequency=2, special_tokens=[
   "<|endoftext|>"
])
print(tokenizer.encode("Wim Dehnke").ids)
tokenizer.save_model(r'C:\tmp\ezlanByteTokenizer')





