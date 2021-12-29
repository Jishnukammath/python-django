from tkinter import *
root=Tk()
f=Frame(root)
f.pack()

Label(f,text="user name : ",fg="red").grid(row=0,column=0)
Entry(f).grid(row=0,column=1)
Label(f,text="password :  : ",fg="red").grid(row=1,column=0)
Entry(f).grid(row=1,column=1)
Button(f, text="login" ,bg="white",).grid(row=2,column=1)

root.mainloop()