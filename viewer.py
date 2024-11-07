from pypdf import PdfReader
from pdf2image import convert_from_path

class PdfViewer:
    def __init__(self, filepath):
        self.pdfpath = filepath

        self.pdf = PdfReader(self.pdfpath)
        self.num_pages = len(self.pdf.pages)

        self.first_page = self.pdf.get_page(0)
        self.page_images = convert_from_path(self.pdfpath)

    def openFile(self, filepath):
        try:
            self.pdf = PdfReader(filepath)
        except:
            print("An error has occured. The file could not be opened.")

        self.num_pages = len(self.pdf.pages)

        self.first_page = self.pdf.get_page(0)
        self.page_images = convert_from_path(self.pdfpath)


    def getPDFImage(self, index):
        return self.page_images[index]




