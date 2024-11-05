from viewer import PdfViewer


def main(): 
    #pdfPath = 'examples/Example-1.pdf'

    print("Please enter the path to your PDF file: ")
    pdfPath = input()
    test = PdfViewer(pdfPath)
    print(test.pdf.get_num_pages())

    test.getPDFImage(0).show()

        
main()

