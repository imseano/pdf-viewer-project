# CPSC 254 Open Source Systems Project - PDF Viewer

A basic PDF viewer created using Python.

### Authors
+ Sean Patrick Oreta
+ Eric Thang
+ Richard Trinh

### Version
Version 1.0<br/>
*Uses Python 3.10 or newer*

### License
GPL 3.0

### Version Changelog
Version 1.0 Features:
+ File menu options
   - Open File: Opens PDF files and displays them.
   - Exit: Exits program
+ Taskbar
    - Page Turning Buttons with Labels
    - Jump To Page Interface
    - Zoom Level Buttons
+ Horizontal and Vertical Scrollbars

## How to Test the Program
***Subject to change***
1. Download the files by clicking on Code ==> Download ZIP.
2. Extract the files.
3. Go to the directory where the pdf_gui.py and viewer.py files are stored.
4. Make sure to install the following dependencies using `pip` or another Python package installer:
   - pypdf
       * Example: `pip install pypdf`
   - pdf2image
       * Example: `pip install pdf2image`
5. Run the pdf_gui.py file using Python 3.10 or later. *It is recommended to use the latest version of Python 3.*
    - If you are on Windows, run `python pdf_gui.py` to test the program.
    - If you are on Mac or Linux, either run `python pdf_gui.py`, `python3 pdf_gui.py`, or `python3.XX pdf_gui.py` where XX would be the version number that you are using (Example: `python3.12 pdf_gui.py`).

From there, you can use the File Menu to open and display a PDF file to test the various buttons.

## Notes on Files used for the PDF Viewer
### PDF GUI - pdf_gui.py
The file is used to create the GUI for the PDF viewer. It can be used alone or another file may use pdf_gui.py file for its PdfGUI class.

If more features are to be added to the PDF viewer, this will be the main file to edit.

#### PdfGUI Class
__init__() -- Initializes all the elements (e.g., taskbar, buttons, etc.) that will be used in the GUI.

load_image() -- Loads in an image of a page of the opened PDF file based on the zoom level that it is set at.

open_file() -- Allows the user to choose a PDF file to open. It is initially set to the current working directory that the pdf_gui.py is in, but the user can navigate elsewhere if the PDF file they want to open is in another location.

display_page() -- Displays a page of the opened PDF file in the window. Displays the page based on the current page number and zoom level. Uses load_image() and update_page_label().

previous_page() -- Goes to the previous page by decrementing the page number and using display_page().

next_page() -- Goes to the next page by incrementing the page number and using display_page().

jump_to_page() -- Allows the user to jump to a specific page via text entry and a button. Uses display_page().

zoom_in() -- Zooms into the page by increments of 10%. Max zoom level is 200%. Uses display_page().

zoom_out() -- Zooms out of the page by decrements of 10%. Minimum zoom level is 10%. Uses display_page().

update_page_label(): Updates information displayed about the current page number and zoom level of the opened PDF file. Called upon by display_page().

on_resize() -- Makes sure that the image stays in center of the canvas upon resizing the window.

###### Dependencies
+ os
+ PIL
+ tkinter
+ viewer via PDFViewer class

### PDF Viewer Backend - viewer.py
The file used to load PDF files and get relevant information for the GUI. This file may be changed if more features are to be added regarding PDF files.

#### PDFViewer Class
__init__(); // Initializes the PdfViewer with a filepath, loads the PDF, counts pages, gets the first page, and generates images for each page.

openFile(); // Opens a new PDF file, handles errors if it cannot open, updates the page count, retrieves the first page, and generates images for each page.

getPDFImage(); // Returns an image of the specified page index in the PDF. This image is returned as an ImageFile, as defined by the Pillow library.


###### Dependencies
+ pdf2image
+ pypdf
