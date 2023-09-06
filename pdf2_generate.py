import PyPDF2

# this module using PyPDF2 3.0.1 version
# generate pdf pages and save in one file

#pdfIn = open('documents.pdf', 'rb')
#pdfReader = PyPDF2.PdfReader(pdfIn)
pdfWriter = PyPDF2.PdfWriter()
num_of_pages = 10
headline = "Hello World"

for pageNum in range(num_of_pages):
    page = PyPDF2.PageObject().create_blank_page(pdfWriter, width=72, height=118)
    # page = pdfReader.pages[pageNum]
    # page.rotate(180)
    pdfWriter.add_page(page)


with open("documents.pdf", mode="wb") as pdfOut:
    pdfWriter.write(pdfOut)
    pdfOut.close()
