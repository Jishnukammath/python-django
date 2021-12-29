from tkinter import *

root=Tk()

entry=Entry()

list_box=Listbox(root).pack()
button=Button(root,text="send")
button.pack(side=BOTTOM)
entry.pack(side=BOTTOM)

root.mainloop()