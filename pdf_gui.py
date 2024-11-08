from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from viewer import PdfViewer

class PdfGUI:
    def __init__(self, master):
        # Master window
        self.master = master
        self.master.title('Basic PDF Viewer')
        self.master.geometry('854x480')
        
        # Menu bar creation
        menu_bar = Menu(self.master)
        
        # File menu commands
        file_menu = Menu(menu_bar, tearoff = 0)
        menu_bar.add_cascade(label = 'File', menu = file_menu)
        
        ### TO-DO: Add command for the Open File command in the file menu. ###
        file_menu.add_command(label = 'Open File', command = None)
        ### END OF TO-DO. ###
        file_menu.add_separator()
        file_menu.add_command(label = 'Exit', command = self.master.destroy)
        
        # Help menu commands
        help_menu = Menu(menu_bar, tearoff = 0)
        menu_bar.add_cascade(label = 'Help', menu = help_menu)
        ### TO-DO: Add commands for the 'Help' and 'About' menu commands in the help menu. ###
        help_menu.add_command(label = 'Help', command = None)
        help_menu.add_command(label = 'About', command = None)
        ### END OF TO-DO. ###
        
        # Configure and display the menu bar.
        self.master.config(menu = menu_bar)
        
        # Task bar creation
        taskbar = Frame(self.master, bg = "lightgrey", height = 30)
        taskbar.pack(side=TOP, fill=X)
    
    ### TO-DO: Add other necessary functions needed for each menu bar command or task bar button we need. ###
    # Note: Place holder functions have already been created. You just need to add the code that will get the job done.
    def open_file():
        pass
    
    def display_page():
        pass
    
    def previous_page():
        pass
    
    def next_page():
        pass
    
    def jump_to_page():
        pass
    
    def zoom_in():
        pass
    
    def zoom_out():
        pass
    ### END OF TO-DO. ###
    
    # Canvas creation for where the pages are going to be displayed.
    
# Root window and mainloop to keep the window open.
app_window = Tk()
application = PdfGUI(app_window)
app_window.mainloop()