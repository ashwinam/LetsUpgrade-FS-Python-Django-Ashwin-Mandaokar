# Put watermark on super.pdf from wtr.pdf

import PyPDF2


template = PyPDF2.PdfFileReader(
    open('Python Scripting/Pdf watermarker/super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(
    open("Python Scripting/Pdf watermarker/pdf/wtr.pdf", "rb"))

output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('Python Scripting/Pdf watermarker/watermarked_output.pdf', 'wb')as file:
        output.write(file)
