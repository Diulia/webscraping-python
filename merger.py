# from PyPDF2 import PdfMerger
from zipfile import ZipFile
import os

file_name = "merged_files.zip"
# merger = PdfMerger()

# for pdf in ["pdf2.pdf", "pdf3.pdf", "pdf4.pdf", "pdf5.pdf"]:
#     merger.append(pdf)

# merger.write("anexos/mergedpdf.pdf")
# merger.close()

def get_all_file_paths(directory):
  
    file_paths = []
  
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
  
    return file_paths 

def main():
    directory = 'anexos/'
    file_paths = get_all_file_paths(directory)

    for file_name in file_paths:
        print(file_name)
  
    with ZipFile('merged_files.zip','w') as zip:
        for file in file_paths:
            zip.write(file)
  
    print('All files zipped successfully!')

if __name__ == "__main__":
    main()