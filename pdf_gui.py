from tkinter import *
from tkinter import filedialog
from viewer import PdfViewer
from PIL import Image, ImageTk
import os

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
        self.file_menu.add_command(label = 'Open File', command = PdfGUI.open_file)
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
        self.canvas = Canvas(self.master, width=854, height=480, bg="white")
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.display_page(0)



    def load_image(self, image):
        image = image.resize((400, 400))  # Resize if necessary
        self.page_image = ImageTk.PhotoImage(image)

        self.canvas.create_image(427, 240, image=self.page_image, anchor = CENTER)
    
    ### TO-DO: Add other necessary functions needed for each menu bar command or task bar button we need. ###
    # Note: Place holder functions have already been created. You just need to add the code that will get the job done.
    # Open files with a prompt that allows the user to select the PDF file they wish to open.
    def open_file():
        # Redundant code that helps ensure that the variables used here are global.
        global current_page, total_pages, pdf_file, images
        filepath = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select a PDF file",
                                              filetypes=(("PDF files", "*.pdf"), ("All Files", "*.*")))
        
        if filepath:
            pdf_file = PdfViewer(filepath)
            total_pages = pdf_file.num_pages
            images = pdf_file.page_images
            current_page = 1
            ### TO-DO: Revert the comment below to code after implementing the display_page function. ###
            ## Comment: The code below gives a hint on what needs to be included as arguments for the display_page function.
            # display_page(images[current_page - 1])
            ### END OF TO-DO. ###
            
    # Displays a single page to the GUI.
    # Updates page label and zoom based on whether the zoom buttons and previous page or next_page button is used.
    def display_page(self, page_number):
        pdf_file = PdfViewer("examples/Example-1.pdf")
        image = pdf_file.getPDFImage(page_number)
        self.load_image(image)
    
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
if __name__ == "__main__":
    app_window = Tk()
    application = PdfGUI(app_window)
    app_window.mainloop()
