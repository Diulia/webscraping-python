import tabula

# df = tabula.read_pdf('anexos/Anexo_I.pdf', pages = 180)[0]
# df.to_csv('anexos/mergedcsv.csv')

pdf_file = 'anexos/Anexo_I.pdf'
multiple_tables = True 
all=True

# table = tabula.read_pdf(pdf_file, pages = 3, multiple_tables=True)
# table[0]

tabula.convert_into(pdf_file, "testecvs.csv", pages = [3, 180])