from tkinter import *
from tkinter import filedialog
from viewer import PdfViewer
from PIL import Image, ImageTk
import os

# Global variables used by the PdfGUI class.
pdf_file = PdfViewer("examples/Example-1.pdf")
current_page = 1
total_pages = pdf_file.num_pages
zoom_level = 1.0
image = None
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

        self.file_menu.add_command(label = 'Open File', command = self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label = 'Exit', command = self.master.destroy)

        # Help menu commands
        self.help_menu = Menu(self.menu_bar, tearoff = 0)
        self.menu_bar.add_cascade(label = 'Help', menu = self.help_menu)
        self.help_menu.add_command(label = 'Help', command = None)
        self.help_menu.add_command(label = 'About', command = None)


        # Configure and display the menu bar.
        self.master.config(menu = self.menu_bar)

        # Task bar creation
        self.taskbar = Frame(self.master, bg = "lightgrey", height = 30)
        self.taskbar.pack(side=TOP, fill=X)

        # Task bar buttons
        ### TO-DO: Add the appropriate commands to the task bar buttons. ###
        self.previous_button = Button(self.taskbar, text = "<<", command = self.previous_page)
        self.previous_button.pack(side=LEFT, padx=2, pady=2)

        self.next_button = Button(self.taskbar, text = ">>", command = self.next_page)
        self.next_button.pack(side=LEFT, padx=2, pady=2)

        self.zoom_in_button = Button(self.taskbar, text = "+", command = self.zoom_in)
        self.zoom_in_button.pack(side=RIGHT, padx=2, pady=2)  

        self.zoom_out_button = Button(self.taskbar, text = "-", command = self.zoom_out)
        self.zoom_out_button.pack(side=RIGHT, padx=2, pady=2)  

        self.page_label = Label(self.taskbar, text=f"Page {current_page} of {total_pages}")
        self.page_label.pack(side=LEFT, padx=2, pady=2)

        self.zoom_label = Label(self.taskbar, text=f"Zoom: {int(zoom_level * 100)}%")
        self.zoom_label.pack(side=RIGHT, padx=2, pady=2)

        # Frame for jump to page controls, placed in the center of the taskbar.
        self.jump_frame = Frame(self.taskbar)
        self.jump_frame.pack(side = TOP, pady = 5)
        self.jump_frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        
        # Jump to Page Label
        self.jump_to_label = Label(self.jump_frame, text = "Jump to Page:")
        self.jump_to_label.pack(side = LEFT)
        
        # Page entry for the Jump to Page interface.
        self.page_entry = Entry(self.jump_frame, width = 5)
        self.page_entry.pack(side = LEFT)
        
        # Jump to Button
        self.jump_to_button = Button(self.jump_frame, text = "Go", command = self.jump_to_page)
        self.jump_to_button.pack(side = LEFT, padx=3, pady=3)
        # Comment: More task buttons can be added later.
        ### END OF TO-DO. ###

        # Scrollbar
        self.x_scrollbar = Scrollbar(self.master, orient = HORIZONTAL)
        self.x_scrollbar.pack(side = BOTTOM, fill = X)
        self.y_scrollbar = Scrollbar(self.master, orient = VERTICAL)
        self.y_scrollbar.pack(side = RIGHT, fill = Y)       

        # Canvas creation to display PDF document pages with scrollbars.
        self.canvas = Canvas(self.master, bg="gainsboro")
        self.canvas.pack(fill=BOTH, expand=True)
        self.canvas.config(xscrollcommand = self.x_scrollbar.set, yscrollcommand = self.y_scrollbar.set)
        self.x_scrollbar.config(command = self.canvas.xview)
        self.y_scrollbar.config(command = self.canvas.yview)

        # Bind the resize event to the canvas.
        self.canvas.bind("<Configure>", self.on_resize)

        self.display_page(0)

    # Takes a PIL Image and displays it on the canvas
    def load_image(self, image):
        global zoom_level, thumbnail
        # If there is no image, simply return nothing.
        if image is None:
            return

        # Force the canvas to update to get the correct information for displaying the page.
        self.canvas.update_idletasks()

        # Set the page image size based on the thumbnail dimensions and zoom level.
        image.thumbnail((400, 400))
        resized_img = image.resize((int(image.width * zoom_level), int(image.height * zoom_level)),
                                   Image.Resampling.LANCZOS)  # Resize if necessary
        self.page_image = ImageTk.PhotoImage(resized_img)

        # Get canvas width and height info to properly display the page in the center of the canvas.
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        # Clear the canvas before displaying the image.
        self.canvas.delete(ALL)

        # Display the image at the center (based on the coordinates) and update the canvas region to be scrollable.
        self.canvas.create_image(int(canvas_width/2), int(canvas_height/2), image=self.page_image, anchor = CENTER)
        self.canvas.config(scrollregion = self.canvas.bbox(ALL))
    

    # Open files with a prompt that allows the user to select the PDF file they wish to open.
    def open_file(self):
        # Redundant code that helps ensure that the variables used here are global.
        global current_page, total_pages, pdf_file
        filepath = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select a PDF file",
                                              filetypes=(("PDF files", "*.pdf"), ("All Files", "*.*")))
        
        if filepath:
            pdf_file = PdfViewer(filepath)
            total_pages = pdf_file.num_pages
            current_page = 1
            self.display_page(current_page - 1)

    # Displays a single page to the GUI.
    # Updates page label and zoom based on whether the zoom buttons and previous page or next_page button is used.
    def display_page(self, page_number):
        global current_page, total_pages, zoom_level, pdf_file, image
        current_page = page_number + 1
        image = pdf_file.getPDFImage(page_number)
        self.load_image(image)
        self.update_page_label()   

    # Command to go to the previous page.
    def previous_page(self):
        global current_page, total_pages
        if current_page > 1:
            current_page -= 1
            self.display_page(current_page - 1)

    # Command to go to the next page.
    def next_page(self):
        global current_page, total_pages
        if current_page < total_pages:
            current_page += 1
            self.display_page(current_page - 1)

    def jump_to_page():
        pass
    
    # Command to zoom in.
    def zoom_in(self):
        global zoom_level, current_page
        if(zoom_level<2.0):#max is 200%
            zoom_level+=.1
        self.display_page(current_page - 1)

    # Command to zoom out.
    def zoom_out(self):
        global zoom_level, current_page
        if(zoom_level>.11):#max is 10%
            zoom_level-=.1
        self.display_page(current_page - 1)

    def update_page_label(self):
        self.page_label.config(text=f"Page {current_page} of {total_pages}")
        self.zoom_label.config(text=f"Zoom: {int(zoom_level * 100)}%")
    
    # Function to reload image upon window or canvas resize.
    def on_resize(self, event):
        self.load_image(image)
    ### END OF TO-DO. ###


# Root window and mainloop to keep the window open.
if __name__ == "__main__":
    app_window = Tk()
    application = PdfGUI(app_window)
    app_window.mainloop()
