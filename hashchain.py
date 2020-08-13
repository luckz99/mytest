from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('Malicious VBA Macro Detection System')

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
