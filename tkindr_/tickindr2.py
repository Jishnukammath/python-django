from tkinter import *
root=Tk()
f=Frame(root)
f.pack()
def sub():
    print("submitedd")
def cancl():
    print("cancel")


Label(f,text ="submit",fg="green").pack()
Button(f, text="login" ,bg="red",command=sub).pack()

Label(f,text ="submit",fg="cyan").pack()
Button(f, text ="Hello", command = cancl).pack()


root.mainloop()