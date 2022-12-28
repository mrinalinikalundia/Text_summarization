# -*- coding: utf-8 -*-
"""Text Summarization using bert, transformer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GrmBDe8h57akoMLNt7VMcTLPvi_w9mcz
"""

!pip install -q bert-extractive-summarizer
!pip install -q spacy==2.1.3
!pip install -q transformer==2.2.2
!pip install -q neuralcoref

from summarizer import Summarizer
from pprint import pprint

with open('/content/Jayaben - Mujeeb Ahmad.txt','r')as file:
  data=file.read().replace('\n', '')

#text summarizer using bert

data=data.replace("\ufeff","")

data[0:1000]

model=Summarizer()

result=model(data,max_length=300,min_length=150)

full=''.join(result)

pprint(full)

#hugging face transformer

from transformers import pipeline

summarizer = pipeline("summarization")

summarizer(full, max_length=130, min_length=30, do_sample=False)

#bert exctractive summarizer

import torch

model1 = Summarizer('distilbert-base-uncased')

import time
start = time.time()
resp=model(data)
end = time.time()

print(f'Response Time: {end-start}')
print(f'Summary: {resp}')

start1 = time.time()
resp1=model1(data)
end1 = time.time()

print(f'Response Time: {end1-start1}')
print(f'Summary: {resp1}')

