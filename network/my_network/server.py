import socket
from tkinter import *
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST_NAME=socket.gethostname()
PORT=12345
s.bind((HOST_NAME,PORT))
s.listen(4)
client,address=s.accept()
def send():
    massage=entry.get()
    listbox.insert("end","server : "+massage)
    entry.delete(0,END)
    client.send(bytes(massage, 'utf-8'))

def recieve():
    massage_from_client = client.recv(50)
    listbox.insert("end","client : "+ massage_from_client.decode('utf-8'))




root=Tk()


listbox=Listbox(root)
listbox.pack()
buttonR=Button(root,text="recieve",command=lambda :recieve())
buttonR.pack(side=BOTTOM)
buttonS=Button(root,text="send",command=lambda :send())
buttonS.pack(side=BOTTOM)
entry=Entry(root)
entry.pack(side=BOTTOM)
root.title("sever")


root.mainloop()
















