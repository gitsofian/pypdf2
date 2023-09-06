import PyPDF2

# this module using PyPDF2 3.0.1 version

# exchange the 'original.pdf' with a name of your file
pdfIn = open('original.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(pdfIn)
pdfWriter = PyPDF2.PdfWriter()
num_of_pages = len(pdfReader.pages)

for pageNum in range(num_of_pages):
    page = pdfReader.pages[pageNum]
    page.rotate(180)
    pdfWriter.add_page(page)

pdfOut = open('rotated.pdf', 'wb')
pdfWriter.write(pdfOut)
pdfOut.close()
pdfIn.close()
