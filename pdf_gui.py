from tkinter import *
from tkinter import filedialog
from viewer import PdfViewer
from PIL import Image, ImageTk

# Global variables used by the PdfGUI class.
current_page = 1
total_pages = 0
zoom_level = 1.0
pdf_file = None
images = None
class PdfGUI:
    def __init__(self, master):
        
        # Master window
        self.master = master
        self.master.title('Basic PDF Viewer')
        self.master.geometry('854x480')
        
        # Menu bar creation
        self.menu_bar = Menu(self.master)
        
        # File menu commands
        self.file_menu = Menu(self.menu_bar, tearoff = 0)
        self.menu_bar.add_cascade(label = 'File', menu = self.file_menu)
        
        ### TO-DO: Add command for the Open File command in the file menu. ###
        self.file_menu.add_command(label = 'Open File', command = None)
        ### END OF TO-DO. ###
        self.file_menu.add_separator()
        self.file_menu.add_command(label = 'Exit', command = self.master.destroy)
        
        # Help menu commands
        self.help_menu = Menu(self.menu_bar, tearoff = 0)
        self.menu_bar.add_cascade(label = 'Help', menu = self.help_menu)
        ### TO-DO: Add commands for the 'Help' and 'About' menu commands in the help menu. ###
        self.help_menu.add_command(label = 'Help', command = None)
        self.help_menu.add_command(label = 'About', command = None)
        ### END OF TO-DO. ###
        
        # Configure and display the menu bar.
        self.master.config(menu = self.menu_bar)
        
        # Task bar creation
        self.taskbar = Frame(self.master, bg = "lightgrey", height = 30)
        self.taskbar.pack(side=TOP, fill=X)
        
        # Task bar buttons
        ### TO-DO: Add the appropriate commands to the task bar buttons. ###
        self.previous_button = Button(self.taskbar, text = "<<", command = None)
        self.previous_button.pack(side=LEFT, padx=2, pady=2)
        
        self.next_button = Button(self.taskbar, text = ">>", command = None)
        self.next_button.pack(side=LEFT, padx=2, pady=2)
    
        self.zoom_in_button = Button(self.taskbar, text = "+", command = None)
        self.zoom_in_button.pack(side=RIGHT, padx=2, pady=2)  
        
        self.zoom_out_button = Button(self.taskbar, text = "-", command = None)
        self.zoom_out_button.pack(side=RIGHT, padx=2, pady=2)  
        
        self.page_label = Label(self.taskbar, text=f"Page {current_page} of {total_pages}")
        self.page_label.pack(side=LEFT, padx=2, pady=2)
        
        self.zoom_label = Label(self.taskbar, text=f"Zoom: {int(zoom_level * 100)}%")
        self.zoom_label.pack(side=RIGHT, padx=2, pady=2)
        
        # Comment: More task buttons can be added later.
        ### END OF TO-DO. ###
        
        # Canvas creation to display PDF document pages.
        self.canvas = Canvas(self.master, bg="white")
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # PDF image
        pdf_file = PdfViewer("examples/Example-1.pdf")
        image = pdf_file.getPDFImage(0)
        image = image.resize((100,100))
        test = ImageTk.PhotoImage(image)
        self.canvas.create_image(10, 10, image = test, anchor = NW)
        pdf_file.getPDFImage(0).show()

        # Position image

    
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
    
    def update_page_label(self):
        self.page_label.config(text=f"Page {current_page} of {total_pages}")
        self.zoom_label.config(text=f"Zoom: {int(zoom_level * 100)}%")
    ### END OF TO-DO. ###
    
# Root window and mainloop to keep the window open.
app_window = Tk()
application = PdfGUI(app_window)
app_window.mainloop()
