from os import listdir
from PyPDF2 import PdfFileMerger



input_dir = "/home/nightingale/Documents/100_Page_Machine_Learning_Book/"

merge_list = []

for x in listdir(input_dir):
    if not x.endswith('.pdf'):
        continue
    merge_list.append(input_dir + x)

merger = PdfFileMerger()

for pdf in merge_list:
    merger.append(pdf)

merger.write(input_dir + '/100_page_ml.pdf')
merger.close()