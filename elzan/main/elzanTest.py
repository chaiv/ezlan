'''
Created on 11.09.2022

@author: vital
'''
#from transformers import pipeline
from transformers import GPT2LMHeadModel
from transformers import GPT2Tokenizer

#pipe = pipeline('text-generation', model=r'C:\tmp\ezlan-gpt',
#                 tokenizer=r'C:\tmp\ezlan-gpt')

#text = pipe("Deimern", max_length=100)[0]["generated_text"]

#print(text)

base_tokenizer = GPT2Tokenizer.from_pretrained(r'C:\tmp\ezlanByteTokenizer')
model = GPT2LMHeadModel.from_pretrained(r'C:\tmp\ezlan-gpt')

text_ids = base_tokenizer.encode("Deimern ist", return_tensors = 'pt')

    # max_length= 50,  
    # do_sample=True,  
    # top_k=100,
    # top_p=0.92,
    # temperature=0.8,
    # repetition_penalty= 1.5,
    # num_return_sequences= 5


generated_text_samples = model.generate(
    text_ids,
    max_length= 50,  
    do_sample=True,  
    top_k=100,
    top_p=0.92,
    temperature=0.8,
    repetition_penalty=1.5,
    num_return_sequences= 5
)

for i, beam in enumerate(generated_text_samples):
    print(f"{i}: {base_tokenizer.decode(beam, skip_special_tokens=True)}")
    print()

