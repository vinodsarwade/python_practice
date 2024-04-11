'''write a program to manipulate pdf files using pypdf. 
your program should be able to merge multiple pdf files into a single pdf file'''

from pypdf import PdfWriter
import os

merger = PdfWriter()
Files = [file for file in os.listdir() if file.endswith(".pdf")]

for pdf in Files:
    merger.append(pdf)

merger.write("Generated_merged-pdf.pdf")
merger.close()