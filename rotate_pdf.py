from PyPDF2 import PdfFileReader, PdfFileWriter

def rotate_pdf(pdf_path):
    pdf_reader = PdfFileReader(pdf_path)
    pdf_writer = PdfFileWriter()

    for i in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(i).rotateClockwise(90)
        pdf_writer.addPage(page)

    with open ("rotate.pdf", 'wb') as rot:
        pdf_writer.write(rot)
