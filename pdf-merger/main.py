import PyPDF2
import sys
import os

merger = PyPDF2.PdfMerger()

for file in os.listdir(os.curdir):
    if (file.endswith('.pdf')):
        fileContent = open(file, 'rb')
        pdfReader = PyPDF2.PdfReader(fileContent)
        merger.append(pdfReader)

merger.write('merged.pdf')
merger.close()