import socket
from tkinter import *
root=Tk()
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST_NAME=socket.gethostname()
PORT=12345
s.connect((HOST_NAME,PORT))

def send():
    massage=entry.get()
    listbox.insert("end","client"+massage)
    entry.delete(0,END)
    s.send(bytes(massage, 'utf-8'))
def receive():
    message = s.recv(100)
    listbox.insert("end", "server : " + message.decode('utf-8'))





listbox=Listbox(root)
listbox.pack()
buttonR=Button(root,text="recieve",command=lambda :receive())
buttonR.pack(side=BOTTOM)
buttonS=Button(root,text="send",command=lambda :send())
buttonS.pack(side=BOTTOM)
entry=Entry(root)
entry.pack(side=BOTTOM)
root.title("client")


root.mainloop()




