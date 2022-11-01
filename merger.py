from PyPDF2 import PdfMerger

merger = PdfMerger()

for pdf in ["anexos/Anexo_I.pdf", "anexos/Anexo_II.pdf", "anexos/Anexo_III.pdf", "anexos/Anexo_IV.pdf"]:
    merger.append(pdf)

merger.write("anexos/mergedpdf.pdf")
merger.close()