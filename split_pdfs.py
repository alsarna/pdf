from PyPDF2 import PdfFileReader, PdfFileWriter
import ntpath

def split_pdfs(pdf_path):
    input_file_name = ntpath.basename(pdf_path)
    pdf_reader = PdfFileReader(pdf_path)
    for page in range(pdf_reader.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf_reader.getPage(page))
        output_file_name = f"{input_file_name}_page_{page + 1}.pdf"

        with open(output_file_name, 'wb') as splt:
            pdf_writer.write(splt)