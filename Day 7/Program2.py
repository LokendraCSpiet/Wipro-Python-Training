"""
Create a class Student(PRN, Name, Age ,Marks ,City).
Write a menu driven program to perform the following functions
1) Accept the details of student
2) Display the details of student
3) Delete the record of student
    a) Delete by PRN
    b) Delete by Name
4) Search the record of student
    a) Search by PRN
    b) Search by Name
    c) search by City
5) Update the record of student
    a) Update the marks of student
    b) Update the name of student
6) Display the student name who scored the highest marks
"""
class Student:
    def __init__(self, PRN, Name, Age ,Marks ,City):
        self.PRN = PRN
        self.Name = Name
        self.Age = Age
        self.Marks = int(Marks)
        self.City = City
    
    def display(self):
        print(f"PRN = {self.PRN}, Name = {self.Name}, Age = {self.Age}, Marks = {self.Marks}, City = {self.City}")

    def update(self,value,type):
        if type == "name":
            self.Name = value
        elif type == "marks":
            self.Marks = value
        else:
            pass

stud = []
while True:
    print("(1) Accept the details")
    print("(2) Display the details")
    print("(3) Delete the record")
    print("(4) Search the record")
    print("(5) Update the record")
    print("(6) Print the record with highest marks")
    print("(7) Exit")
    ch = int(input("Enter Your Choice: "))
    print()
    match ch:
        case 1:
            # Accept the details of student
            PRN   = input("Enter Your PRN: ")
            Name  = input("Enter Your Name: ")
            Age   = input("Enter Your Age: ")
            Marks = input("Enter Your Marks: ")
            City  = input("Enter Your City: ")
            obj = Student(PRN, Name, Age ,Marks ,City)
            stud.append(obj)
        case 2:
            # Display the details of student
            for i in stud:
                i.display()
        case 3:
            # Delete the record of student
            print("A) Delete by PRN\nB) Delete by Name")
            choice = input("Enter your choice: ").upper()
            match choice:
                case "A":
                    flag = True
                    prn = input("Enter PRN: ")
                    for i in stud:
                        if i.PRN == prn:
                            stud.remove(i)
                            flag = False
                    if flag:
                        print("PRN is not Present")
                case "B":
                    flag = True
                    name = input("Enter Name: ")
                    for i in stud:
                        if i.Name == name:
                            stud.remove(i)
                            flag = False
                    if flag:
                        print("Name is not Present")
                case _:
                    print("Invalid Choice")
        case 4:
            # Search the record of student
            print("A: Search By PRN")
            print("B: Search By City")
            choice = input("Enter your choice: ").upper()
            match choice:
                case "A":
                    flag = True
                    prn = input("Enter PRN: ")
                    for i in stud:
                        if i.PRN == prn:
                            i.display()
                            flag = False
                    if flag:
                        print("PRN is not Present")
                case "B":
                    flag = True
                    city = input("Enter City: ")
                    for i in stud:
                        if i.City == city:
                            i.display()
                            flag = False
                    if flag:
                        print("City is not Present")
                case _:
                    print("Invalid Choice")
        case 5:
            # Update the record of student
            print("A: Update the marks of student")
            print("B: Update the name of student")
            choice = input("Enter your choice: ").upper()
            prn = input("Which student data enter prn: ")
            match choice:
                case "A":
                    flag = True
                    marks = input("Enter marks: ")
                    for i in stud:
                        if i.PRN == prn:
                            i.Marks = marks
                            flag = False
                    if flag:
                        print("Student is not Present")
                case "B":
                    flag = True
                    name = input("Enter name: ")
                    for i in stud:
                        if i.PRN == prn:
                            i.Name = name
                            flag = False
                            break
                    if flag:
                        print("PRN is not Present")
                case _:
                    print("Invalid Choice")
        case 6:
            # Display the student name who scored the highest marks
            m = 0
            for i in stud:
                if i.Marks > m:
                    m = i.Marks
            for i in stud:
                if m == i.Marks:
                    i.display()
        case 7:
            break
        case _:
            print("Invalid Choice")
    print()