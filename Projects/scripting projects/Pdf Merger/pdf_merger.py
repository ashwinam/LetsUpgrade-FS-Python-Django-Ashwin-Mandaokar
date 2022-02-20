import PyPDF2
import sys

# Project is about combining the pdf files into one
# take inputes from terminal
inputs = sys.argv[1:]

# create a function for pdf merger


def pdf_merger(PDFs):
    merger = PyPDF2.PdfFileMerger()
    for pdf in PDFs:
        print(pdf)
        merger.append(pdf)
    merger.write("super.pdf")


pdf_merger(inputs)
