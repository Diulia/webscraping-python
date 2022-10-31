from PyPDF2 import PdfReader

reader = PdfReader("anexos/Anexo_I.pdf")
page = reader.pages[3]
print(page.extract_text(0))