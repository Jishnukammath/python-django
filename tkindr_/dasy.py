from tkinter import *
import parser
root=Tk()
root.title("DAYS CALCULATOR")
display=Entry(root)
root.geometry('400x400')

# display.grid(row=1,columnspan=6)
# Button(root,text="Get").grid(row=1,column=9)


Label(root,text="month : ").grid(row=1,column=2)
display.grid(row=2,column=2)


Label(root,text="year : ").grid(row=1,column=4)
display.grid(row=2,column=4)

root.mainloop() 




