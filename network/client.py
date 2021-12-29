# server client communication

# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# HOST_NAMW=socket.gethostname()
# PORT=1232
# s.connect((HOST_NAMW,PORT))




#building msg functionality


import socket

from tkinter import *
root=Tk()



def send(listbox,entry):
    message=entry.get()
    listbox.insert("end","client : "+message)
    entry.delete(0, END)
    s.send(bytes(message, 'utf-8'))
    receive(listbox)

def receive(listbox):
    message2 = s.recv(100)
    listbox.insert("end","server : " + message2.decode('utf-8'))




entry=Entry()

listbox=Listbox(root)
listbox.pack()
button=Button(root,text="send",command=lambda :send(listbox,entry))
rbutton=Button(root,text="recieve",command=lambda :receive(listbox))
button.pack(side=BOTTOM)
rbutton.pack(side=BOTTOM)
entry.pack(side=BOTTOM)
root.title("client")

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST_NAME=socket.gethostname()
PORT=1232
s.connect((HOST_NAME,PORT))

root.mainloop()











