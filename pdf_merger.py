from os import listdir
from PyPDF2 import PdfFileMerger


# put input directory here
input_dir = "/path/to/pdf/files/"

merge_list = []

for x in listdir(input_dir):
    if  x.endswith('.pdf'):
        merge_list.append(input_dir + x)

merger = PdfFileMerger()

for pdf in merge_list:
    merger.append(pdf)

merger.write(input_dir + '/merged_file.pdf')
merger.close()
print('Merging Success')