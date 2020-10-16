from tkinter import *

import socket 

root = Tk()
root.title('Malicious VBA Macro Detection System')
root.geometry('800x600')

message = Label(root, text="1234")
message.pack() 

def connect_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('192.168.0.177',2020))

    client.send(bytes('I am Client', 'utf8'))

    from_serv = client.recv(4096)

    client.close()
    message.config(text=from_serv)

button = Button(root, text='Connect Server', command=connect_server)
button.pack() 

root.mainloop()
