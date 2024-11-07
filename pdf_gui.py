from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from viewer import PdfViewer

class PdfGUI:
    def __init__(self, master):
        self.master = master
        self.master.title('Basic PDF Viewer')
    
    def open():
        pass
    

app_window = Tk()
application = PdfGUI(app_window)
app_window.mainloop()