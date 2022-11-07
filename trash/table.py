from PyPDF2 import PdfFileReader
import pandas as pd

pdfObject = open('./anexos/Anexo_I.pdf')

pdfReader = PdfFileReader(pdfObject)
text=''
for i in range(0,pdfReader.numPages):
    pageObject = pdfReader.getPage(i)
    text += pageObject.extractText()
print(text)


