import PyPDF2
with open("E:/PythonProject/pdfplayground/dummy.pdf","rb") as file:
   reader = PyPDF2.PdfFileReader(file)
   page = reader.getPage(0)
   page.rotateClockwise(90)
   writer = PyPDF2.PdfFileWriter()
   writer.addPage(page)
   with open("E:/PythonProject/pdfplayground/tilt.pdf","wb") as new_file:
      writer.write(new_file)