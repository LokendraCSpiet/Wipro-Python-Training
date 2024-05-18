class ABC:
    def __init__(self):
        print("In init of ABC")

    def display(self):
        print("In class ABC")

class XYZ(ABC):
    def __init__(self):
        super().__init__()
        print("In init of XYZ")

    def display(self):
        super().display()
        print("In class XYZ")

class PQR(XYZ):
    def __init__(self):
        super().__init__()
        print("IN init of PQR")

    def display(self):
        super().display()
        print("In class PQR")

obj = PQR()
obj.display()
        