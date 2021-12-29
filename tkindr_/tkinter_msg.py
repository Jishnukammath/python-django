from tkinter import *
import tkinter.messagebox
root=Tk()

# tkinter.messagebox.showinfo("show ifo","are you sure")
var=tkinter.messagebox.askquestion("show ifo","are you sure")\

# showwarnig
# showerror
# askokcancel
# askokno
# askretrycancle

if var=="yes":
    print("yes")
else:
    print("no")





root.mainloop()