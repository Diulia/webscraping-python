import pdfplumber
import pandas as pd

file = 'anexos/Anexo_I.pdf'

lines = []

with pdfplumber.open(file) as pdf:
    pages = pdf.pages
    for page in pdf.pages:
        text = page.extract_text()
        lines.append(text)
            # print(line)

df = pd.DataFrame(lines)
df.to_csv('teste.csv')

