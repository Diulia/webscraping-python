import pandas as pd
import tabula


df = tabula.read_pdf('anexos/Anexo_I.pdf', pages = 180, columns= (1,2,3,4,5,6,7,8,9.10,11,12,13))[0]
print(df)
df.to_csv('telsst.csv')
