class student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def getDtata(self):
        self.name=str(input("enter your name : "))
        self.mark=int(input("enter your mark : "))
    def display(self):
        print(self.name,"\n",self.mark)

obj=student("","")
obj.getDtata()
obj.display()