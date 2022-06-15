from ast import keyword
from numpy import sort
import pdfplumber
import os
import re



def extract_data():

  files = os.listdir('/Users/wyatthoffman/Documents/uprecruit/prospects/')
  

  for file in files:
    if '.DS_Store' in file:
      print('skipped')
    with pdfplumber.open(f'/Users/wyatthoffman/Documents/uprecruit/prospects/{file}') as pdf:
      pdf_text = ''
      print(file)
      for page in pdf.pages:
        pdf_text += page.extract_text()
      split_txt = re.split(r'\W+', pdf_text.lower())
      data = {}
      for word in split_txt:
        print(split_txt)
      # #   if word == '':
      #     continue
      #   if word not in data:
      #     data[word] = 0
      #   data[word] += 1
      # keywords = ['java', 'php', 'laravel', 'aws']
      # for key in keywords:
      #   if key not in data:
      #     print(f'{key} : 0')
      #   else:
      #     print(f'{key} : {data[key]}')
      # print('\n')

extract_data()
