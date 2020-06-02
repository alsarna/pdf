from PyPDF2 import  PdfFileReader, PdfFileWriter

def merge_pdfs(output_pdf_path, *paths):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf = PdfFileReader(path)
        for page in range(pdf.getNumPages()):
            pdf_writer.addPage(pdf.getPage(page))

    with open(output_pdf_path, 'wb') as out:
        pdf_writer.write(out)