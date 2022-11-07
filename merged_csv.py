from zipfile import ZipFile
import os

file_name = "merged_files.zip"

def get_all_file_paths(directory):
  
    file_paths = []
  
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
  
    return file_paths 

def main():
    directory = '/'
    file_paths = ["teste_diulia.csv"]

    for file_name in file_paths:
        print(file_name)
  
    with ZipFile('Teste_Diulia.zip','w') as zip:
        for file in file_paths:
            zip.write(file)
  
    print('All files zipped successfully!')

if __name__ == "__main__":
    main()