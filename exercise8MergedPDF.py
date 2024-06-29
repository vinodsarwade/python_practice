'''write a program to manipulate pdf files using pypdf. 
your program should be able to merge multiple pdf files into a single pdf file'''

from PyPDF2 import PdfWriter
import os
pdf_directory = "C:/Users/VSARWADE/Desktop/python/Files"
output_merger = PdfWriter()
Files = [os.path.join(pdf_directory,file) for file in os.listdir(pdf_directory) if file.endswith(".pdf")]

for pdf in Files:
        with open(pdf,"rb") as file:
            output_merger.append(pdf)
output_merger.write("Generated_merged-pdf.pdf")
output_merger.close()



'''AI'''
# from PyPDF2 import PdfWriter, PdfReader
# import os
# pdf_directory = "C:/Users/VSARWADE/Desktop/python/Files"
# output_pdf = PdfWriter()
# pdf_files = [os.path.join(pdf_directory, file) for file in os.listdir(pdf_directory) if file.endswith(".pdf")]

# for pdf in pdf_files:
#     try: 
#         with open(pdf, "rb") as file:
#             reader = PdfReader(file)
#             for page in reader.pages:
#                 output_pdf.add_page(page)
#     except Exception as e:
#         print(f"Error processing {pdf}: {e}")
# # Write the merged PDF to a new file
# output_filename = "Generated_merged-pdf.pdf"
# print("Merged PDF file generated successfully!")




