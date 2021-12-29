from tkinter import *
root=Tk()


mymenu=Menu(root)
root.config(menu=mymenu)

submenu=Menu(mymenu)

mymenu.add_cascade(label="file",menu=submenu)
submenu.add_command(label="save")
submenu.add_separator()
submenu.add_command(label="save as")


submenu1=Menu(mymenu)

mymenu.add_cascade(label="edit",menu=submenu1)
submenu1.add_command(label="redo")
submenu1.add_separator()
submenu1.add_command(label="undo")






root.mainloop()