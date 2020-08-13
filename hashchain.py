from tkinter import *

number1 = 9
number2 = 8
word1 = "Kappa!"

root = Tk()

#Creating a Label Widget
myLabel = Label(root, text="Hello World!\nHello You!\nHello My fren!\n" + word1)

#Shoving it onto the screen
myLabel.pack()

root.mainloop()
