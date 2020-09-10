import os, sys
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import time

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


def open1():
    global my_label
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("png files", "*.png"),("all files", "*.*")))
    my_label = Label(root, text=root.filename)
    my_label.grid(row=0,column=2)

    
my_btn = Button(root, text="Open File", command=open1).grid(row=3,column=0)

#This is for a text box with scroll bar
scroll_frame = Frame(root)
my_scrollbar= Scrollbar(scroll_frame, orient=VERTICAL)

#configure scrollbar
my_text = Text(scroll_frame, width=10, height=10, yscrollcommand=my_scrollbar.set)
my_text.insert(INSERT, "hi\nhi\nhi\nhi\nhi\nhi\nhi\nhi\nhi\nhi\nno\nno\nno\nhi\nji\nji\nji\nji\nji\nji")
my_text.config(state="disabled")
my_scrollbar.config(command=my_text.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
scroll_frame.grid(row=10, column=10)
my_text.pack(pady=15)

#scanning directory
def open_dir():
    pass

my_btn = Button(root, text="Open Directory", command=open_dir).grid(row=4,column=0)

#this is to write to file beware of the 'open' keyword, some fucntions might have the same name
def write_file():
    text_file = open("sameple.txt", "w")
    text_file.write('xxxxx')
    text_file.close()

textbox = Text(root, width=40, height=10)
textbox.grid(row=5,column=0)

write_button = Button(root, text="save", command=write_file)
write_button.grid(row=6,column=0)

#treeview

def remove_one():
    x = treev.selection()[0]
    my_text.insert(INSERT, treev.item(x)["values"][0])

treev = ttk.Treeview(root, selectmode='browse')
treev.grid(row=7,column=0)

treev["columns"] = ("1", "2", "3")
treev['show'] = 'headings'

treev.column("1", width = 90, anchor ='c') 
treev.column("2", width = 90, anchor ='se') 
treev.column("3", width = 90, anchor ='se')

treev.heading("1", text ="Name") 
treev.heading("2", text ="Sex") 
treev.heading("3", text ="Age")

treev.insert("", 'end', text ="L11222",  
             values =("Nidhi", "F", "25")) 
treev.insert("", 'end', text ="L2", 
             values =("Nisha", "F", "23")) 
treev.insert("", 'end', text ="L3", 
             values =("Preeti", "F", "27"))

delete_record = Button(root, text='delete record', command=remove_one)
delete_record.grid(row=7, column=1)

my_text = Text(root)
my_text.insert(1.0,"ABCDEFGGGG")
my_text.config(state='disabled')
my_text.grid(row=7, column=2)

def copy():
    root.clipboard_clear()
    root.clipboard_append(my_text.get(1.0, END))

copy_button = Button(root, text='copy', command=copy)
copy_button.grid(row=7,column=3)

#Time
def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    ampm = time.strftime("%p")
    timezone = time.strftime("%Z")

    time_label.config(text= timezone + "\t" + hour + ":" + minute + ":" + second + " " + ampm)
    time_label.after(1000, clock)

def update():
    time_label.config(text="New test")


time_label = Label(root, text="")
time_label.grid(row=8, column=0)

copy_label = Label(root, text="")
copy_label.grid(row=7, column=4)


clock()

#create a new window
def open_help():
    top = Toplevel()
    top.title('Help Manual')
    lbl = Label(top, text="Hello World").pack()
    btn2 =  Button(top, text='close window', command=top.destroy)
    btn2.pack()

help_btn = Button(root, text= "help manual", command=open_help)
help_btn.grid(row=9, column=0)


root.mainloop()
