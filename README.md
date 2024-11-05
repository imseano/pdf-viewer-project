# CPSC 254 Open Source Systems Project - PDF Viewer

Note on PDFViewer class:

__init__(); // Initializes the PdfViewer with a filepath, loads the PDF, counts pages, gets the first page, and generates images for each page.

openFile(); // Opens a new PDF file, handles errors if it cannot open, updates the page count, retrieves the first page, and generates images for each page.

getPDFImage(); // Returns an image of the specified page index in the PDF. This image is returned as an ImageFile, as defined by the Pillow library.


Dependencies: 
pdf2image
pypdf
