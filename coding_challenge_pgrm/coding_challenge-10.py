class Computer:
    def __init__(self,spec1,sepc2,spec3):
        self.spec1=spec1
        self.spec2=sepc2
        self.spec3=spec3
    def getSpecs(self):
        self.spec1=str(input("Enter computer specification : "))
    def displaySpec(self):
        print("computer specification : ",self.spec1)

class Desktop(Computer):
    def getDesktopSpecs(self):
        self.sepc2 = str(input("Enter Desktop specifications : "))

    def displayDesktopSpec(self):
        print("Desktop specifications : ",self.sepc2)

class Laptop(Desktop):

    def getLaptopSpecs(self):
        self.spec3 = str(input("enter Laptop specifications : "))

    def displayLaptopSpec(self):
        print("Laptop specifications : ",self.spec3)

obj=Laptop("","","")
obj.getSpecs()
obj.getDesktopSpecs()
obj.getLaptopSpecs()
obj.displaySpec()
obj.displayDesktopSpec()
obj.displayLaptopSpec()