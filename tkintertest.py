from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('Malicious VBA Macro Detection System')

#Initiating the menu
my_menu = Menu(root)
root.config(menu=my_menu)

def our_command():
    pass

#hide all frame
def hide_all_frames():
    for widget in frame.winfo_children():
        widget.destroy()

    frame.pack_forget()

#Create a menu item
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New...", command=our_command)
file_menu.add_separator()
file_menu.add_command(label="Exit...", command=root.quit)

#create an edit menu
help_menu = Menu(my_menu)
my_menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Walkthrough", command=our_command)

#Create an frame
frame = LabelFrame(root, padx=20, pady=20)
frame.grid(row=0,column=4)

#Create an item inside the fram
b = Button(frame, text="Dont Click Here")
b.grid(row=0, column=0)

#Creating an image button
detect_btn = PhotoImage(file='search_small.png')
ScanFolder_btn = PhotoImage(file='search_small.png')
#img_label = Label(image=detect_btn)
#img_label.grid(row=1, column=6)

def thing():
    mylabel4.config(text="You clicked the button......")

my_button = Button(root, image=detect_btn, command=thing, borderwidth=0)
my_button.grid(row=0, column=0, padx=20, pady=20)

my_button2 = Button(root, image=ScanFolder_btn, command=thing, borderwidth=0)
my_button2.grid(row=0, column=1,padx=20, pady=20)

mylabel4 = Label(root, text='Can you change me')
mylabel4.grid(row=1,column=1)


#Creating a Label Widget
myLabel1 = Label(root, text="Hello World!\nHello You!")

#Displaying it onto the screen
myLabel1.grid(row=4,column=0)


def open():
    global my_label
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("png files", "*.png"),("all files", "*.*")))
    my_label = Label(root, text=root.filename)
    my_label.grid(row=0,column=2)

    
my_btn = Button(root, text="Open File", command=open).grid(row=3,column=0)



root.mainloop()
