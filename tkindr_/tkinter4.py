from tkinter import *
class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    self.button = Button(frame,
                         text="QUIT", fg="red",
                         command=frame.quit).pack()

    self.slogan = Button(frame,
                         text="Hello",
                         command=self.write_slogan).pack()

  def write_slogan(self):
    print ("Tkinter is easy to use!")

root = Tk()
app = App(root)
root.mainloop()




