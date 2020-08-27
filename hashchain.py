from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('Malicious VBA Macro Detection System')

#Initiating the menu
my_menu = Menu(root)
root.config(menu=my_menu)

def our_command():
    pass

#Create a menu item
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New...", command=our_command)
file_menu.add_separator()
file_menu.add_command(label="Exit...", command=root.quit)

#create an edit menu
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=our_command)
edit_menu.add_separator()
edit_menu.add_command(label="Copy", command=our_command)


#Creating a Label Widget
myLabel1 = Label(root, text="Hello World!\nHello You!\nHello My fren!")
myLabel2 = Label(root, text="My name is luckzzzzz")
myLabel3 = Label(root, text="asdasdasd")

#Shoving it onto the screen
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=5)
myLabel3.grid(row=1,column=3)


def open():
    global my_label
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("png files", "*.png"),("all files", "*.*")))
    my_label = Label(root, text=root.filename)
    my_label.grid(row=0,column=2)

    
my_btn = Button(root, text="Open File", command=open).grid(row=0,column=1)



root.mainloop()
