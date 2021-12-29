class A:
    def __init__(self,name,mark,age,subject):
        self.name=name
        self.age=age
        self.mark=mark
        self.subject=subject
    def getName(self):
        self.name=input("enter your name : ")
class B(A):
    def getMark(self):
        self.mark=int(input("enter your mark : "))

class C(B):
    def getAge(self):
        self.age=int(input("enter your age : "))
class D(C):
    def getSub(self):
        self.subject=str(input("enter you subject name : "))

class E(D):
    def display(self):
        print(self.name)
        print(self.mark)
        print(self.age)
        print(self.subject)



obj=E(""," ","","")
obj.getName()
obj.getMark()
obj.getAge()
obj.getSub()
obj.display()