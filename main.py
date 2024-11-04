from pypdf import PdfReader
from pdf2image import convert_from_path

class PdfViewer:
    def __init__(self, filepath):
        self.pdfpath = filepath

        self.pdf = PdfReader(self.pdfpath)
        self.num_pages = len(self.pdf.pages)

        self.first_page = self.pdf.get_page(0)
        self.page_images = convert_from_path(self.pdfpath)

    def openFile(self):
        print("hi")

    def getPDFImage(self, index):
        return self.page_images[index]



 
def main(): 
    pdfPath = 'examples/Example-1.pdf'

    test = PdfViewer(pdfPath)
    print(test.pdf.get_num_pages())

    test.getPDFImage(0).show()

        
main()

