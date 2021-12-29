# server client communication

# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# HOST_NAME=socket.gethostname()
# PORT=1232
# s.bind((HOST_NAME,PORT))
# s.listen(4)
#
# while True:
#     client,address=s.accept()
#     print(address)


#building msg functionality

#
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# HOST_NAME=socket.gethostname()
# PORT=1232
# s.bind((HOST_NAME,PORT))
# s.listen(4)
# client, address = s.accept()
# while True:
#     msg=input("server : ")
#     client.send(bytes(msg,'utf-8'))
#     msg_frm_client=client.recv(50)
#     print("client : ",msg_frm_client.decode('utf-8'))







#send massage to clinet



import socket
from tkinter import *
root=Tk()



def send(listbox,entry):
    message1=entry.get()
    listbox.insert("end","server : "+message1)
    entry.delete(0, END)
    client.send(bytes(message1, 'utf-8'))


def receive(listbox):
    msg_frm_client = client.recv(50)
    listbox.insert("end","client : "+msg_frm_client.decode('utf-8'))




entry=Entry()

listbox=Listbox(root)
listbox.pack()
abutton=Button(root,text="send",command=lambda :send(listbox,entry))
bbutton=Button(root,text="recieve",command=lambda :receive(listbox))
abutton.pack(side=BOTTOM)
bbutton.pack(side=BOTTOM)
entry.pack(side=BOTTOM)
root.title("server")







s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST_NAME=socket.gethostname()
PORT=1232
s.bind((HOST_NAME,PORT))
s.listen(4)
client, address = s.accept()



root.mainloop()









