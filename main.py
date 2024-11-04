from pypdf import PdfReader
from pdf2image import convert_from_path

def main():
    print('hello world')
    pdfPath = 'examples/Example-1.pdf'
    reader = PdfReader(pdfPath)
    print(reader.get_num_pages())

    pageObj = reader.get_page(0);

    print(pageObj.extract_text());

    page_image = convert_from_path(pdfPath)
    page_image[0].show()


main()
