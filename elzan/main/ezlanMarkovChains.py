#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
Created on 05.10.2022

@author: vital
'''
import markovify


with open(r'C:\Users\vital\git\transformers\examples\pytorch\language-modeling\DialogeNurSelbst.txt',encoding='UTF8') as f:
    text = f.read()


text_model = markovify.Text(text)

for i in range(10):
    print(text_model.make_sentence())
