from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from viewer import PdfViewer

class PdfGUI:
    def __init__(self, master):
        self.master = master
        self.master.title('Basic PDF Viewer')
        self.master.geometry('854x480')
        
        menu_bar = Menu(self.master)
        
        file_menu = Menu(menu_bar, tearoff = 0)
        menu_bar.add_cascade(label = 'File', menu = file_menu)
        file_menu.add_command(label = 'Open File', command = None)
        file_menu.add_separator()
        file_menu.add_command(label = 'Exit', command = self.master.destroy)
        
        help_menu = Menu(menu_bar, tearoff = 0)
        menu_bar.add_cascade(label = 'Help', menu = help_menu)
        help_menu.add_command(label = 'Help', command = None)
        help_menu.add_command(label = 'About', command = None)
        
        self.master.config(menu = menu_bar)
    
    def open_file():
        pass
    

app_window = Tk()
application = PdfGUI(app_window)
app_window.mainloop()