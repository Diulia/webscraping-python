# from PyPDF2 import PdfReader
from PyPDF2 import PdfFileReader


# reader = PdfReader("anexos/Anexo_I.pdf")
# page = reader.pages[3]
# print(page.extract_text(0))

pdfObject = open('./anexos/Anexo_I.pdf', 'rb')

pdfReader = PdfFileReader(pdfObject)
text=''
for i in range(0,pdfReader.numPages):
    pageObject = pdfReader.getPage(i)
    text += pageObject.extractText()
print(text)