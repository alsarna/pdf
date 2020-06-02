from PyPDF2 import PdfFileReader

def extract_info(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PdfFileReader(file)
        info = pdf_reader.getDocumentInfo()
        count_pages = pdf_reader.getNumPages()

    print(info)
    print(count_pages)
