class myClass:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def display(self):  # self always points to the current object of the class
        print(self.a, " ", self.b)
    
    def display2(arya):
        print(arya.a, " ", arya.b)

obj1 = myClass(100,200)
obj2 = myClass(30,40)
obj3 = myClass(10,20)

obj1.display()
obj3.display()
myClass.display(obj2)

# obj1.display2()
# obj3.display2()
# myClass.display2(obj2)
