import PyPDF2

# with open('dummy.pdf', 'rb') as file:  # read binary
#     reader = PyPDF2.PdfFileReader(file)
#     print(reader.numPages)
#     print(reader.getPage) # get the page object.
#     page = reader.getPage(0)
#     page.rotateCounterClockwise(90))
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('rotated.pdf', 'wb') as new_file: # write binary
#         writer.write(new_file)


from pdf2image import convert_from_path
pages = convert_from_path('pier.pdf', 500)

# Saving pages in jpeg format
for page in pages:
    page.save('pier.jpg', 'JPEG')
