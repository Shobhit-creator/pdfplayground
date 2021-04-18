import PyPDF2

template = PyPDF2.PdfFileReader(open("E:\PythonProject\pdfplayground\super.pdf","rb"))
watermark = PyPDF2.PdfFileReader(open("E:\PythonProject\pdfplayground\wtr.pdf","rb"))
output = PyPDF2.PdfFileWriter()

for i in range(template.numPages):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)
with open("E:\PythonProject\pdfplayground\watermark_output.pdf","wb") as file:
    output.write(file)