"""
Define the class Employee with following fields:
Employee id, Employee name, Salary, Age, Gender, City, Department Name, Designation, Pan Card number, Aadhar number.
1. Add the record of Employee 
2. Delete the record of Employee 
3. Update Employee Details
    a. Update name of Employee 
    b. Update address of Employee 
    c. Update Salary of Employee
        i. Update the salary of specific Employee by Employee id.
        ii. Update the salary of all Employees working in
            specificdepartment
        iii. Update the salary of all Employees.
4. Search details of Employee
    a. Search by Employee id
    b. Search by Employee name
    c. Search by Department name
5. Display the details of Employee with highest salary 
6. Display the details of Employee with lowest salary
"""
class Employee:
    def __init__(self,Id,name,salary,city,age,gender,department,designation,pan,aadhar):
        self.emp_id=Id
        self.emp_name=name
        self.emp_salary=salary
        self.emp_age=age
        self.emp_city=city
        self.emp_gender=gender
        self.emp_department=department
        self.emp_designation=designation
        self.emp_pan=pan
        self.emp_aadhar=aadhar

    def display(self):
        print(f"ID: {self.emp_id}, Name: {self.emp_name}, Gender: {self.emp_gender}, Age:{self.emp_age}, Ciyt: {self.emp_city}, Salary: {self.emp_salary} Department : {self.emp_department}, Dsignation: {self.emp_designation}")


employees=[]
while True:
    print("----------------------------------------")
    print(" 1: Add Records \n 2: Display Employee's Details \n 3: Delet Records \n 4: Search Employee Details \n 5: Update Details\n 6: Highest Salary\n 7: Lowest Salary\n 8: Exit")
    opt=input("Enter Your Choice: ")
    print("----------------------------------------")
    match opt:
        case "1":
            print("Enter Employee Details")
            Id=input("Enter ID:")
            name=input("Enter Name:")
            gender=input("Enter Gender:")
            age=input("Enter Age:")
            city=input("Enter City:")
            department=input("Enter Department Name: ")
            designation=input("Enter Designation: ")
            salary=input("Enter your Salary: ")
            pan=input("Enter Pan No. : ")
            aadhar=input("Etner Aadhar No.: ")
            obj=Employee(Id,name,salary,city,age,gender,department,designation,pan,aadhar)
            employees.append(obj)
            print("Registered Successfully")
        case "2":
            print("EMPLOYEE'S DETAILS")
            for i in employees:
                i.display()
        case "3":
            print("REMOVE EMPLOYEE")
            print(" A: BY ID \n B: BY Name")
            c=input("Enter your Choice: ").upper()
            match c:
                case "A":
                    flag=True
                    id=input("Enter ID: ")
                    for i in employees:
                        if i.emp_id==id:
                            employees.remove(i)
                            flag=False
                            print("Removed successfully")
                    if flag:
                        print("No Employee Found with this ID")
                        
                case "B":
                    flag=True
                    name=input("Enter Name: ").upper()
                    for i in employees:
                        if i.emp_name==name:
                            employees.remove(i)
                            flag=False
                            print("Removed successfully")
                    if flag:
                        print("No Employee Found with this Name")
                case _:
                        print("Invalid Choice")
        case "4":
            print("SEARCH Employee")
            print(" A: BY ID\n B: BY NAME\n C: BY DEPARTMENT")
            c=input("Enter your Choice: ").upper()
            match c:
                case "A":
                    flag=True
                    id=input("Enter ID: ")
                    for i in employees:
                        if i.emp_id==id:
                            i.display()
                            flag=False
                    if flag:
                        print("No Employee found with this Id")
                case "B":
                    flag=True
                    name=input("Enter Name: ").upper()
                    for i in employees:
                        if i.emp_name==name:
                            i.display()
                            flag=False
                    if flag:
                        print("No employee found with this name")
                case "C":
                    flag=True
                    dept=input("Enter Department Name: ").upper()
                    for i in employees:
                        if i.emp_department==dept:
                            i.display()
                            flag=False
                    if flag:
                        print("No employees found Form this Department")
                case _:
                        print("Invalid Choice")

        case "5":
            print("UPATE RECORDS")
            print(" A: Update Name\n B: Update Address\n C: Update Salary")
            c=input("Enter your Choice: ").upper()
            match c:
                case "A":
                    d=input("Enter ID of Employee: ")
                    flag=True
                    for i in employees:
                        if i.emp_id==d:
                            name=input("Enter Updated Name: ")
                            i.emp_name=name
                            flag=False
                            print("Name Updated")
                    if flag:
                        print("No Employee found with this ID")
                case "B":
                    d=input("Enter ID of Employee: ")
                    flag=True
                    for i in employees:
                        if i.emp_id==d:
                            name=input("Enter Updated City: ").upper()
                            i.emp_city=name
                            flag=False
                            print("Address Updated")
                    if flag:
                        print("No employee found with this ID")
                case "C":
                    print("UPDATE SALARY")
                    print(" A: Salary of Employee\n B: Employees Under Department\n C: All Employees")
                    opt=input("Enter your coise: ").upper()
                    match opt:
                        case "A":
                            flag=True
                            d=input("Enter ID of Employee: ")
                            for i in employees:
                                if i.emp_id==d:
                                    name=input("Enter Updated Salary: ")
                                    i.emp_salary=name
                                    flag=False
                                    print("Salary Updated")
                            if flag:
                                print("No Employee found with this ID")
                        case "B":
                            flag=True
                            d=input("Enter Department Name: ")
                            name=input("Enter Updated Salary: ")
                            for i in employees:
                                if i.emp_department==d:
                                    i.emp_salary=name
                                    flag=False
                            if flag:
                                print("No Employee found within this Department")
                            else:
                                print("Salary Updated")
                        case "C":
                            name=input("Enter Updated Salary: ")
                            for i in employees:
                                i.emp_salary=name
                        case _:
                            print("Invalide Choice")
                case _:
                        print("Invalid Choice")
        case "6":
            print("EMPLOYEES WITH HIGHEST SALARY")
            m=0
            for i in employees:
                if int(i.emp_salary)>m:
                    m=int(i.emp_salary)
            for i in employees:
                if int(i.emp_salary)==m:
                    i.display()
        case "7":
            print("EMPLOYEES WITH LOWEST SALARY")
            l=int(employees[0].emp_salary)
            for i in employees:
                if int(i.emp_salary)<l:
                    l=int(i.emp_salary)
            for i in employees:
                if int(i.emp_salary)==l:
                    i.display()
        case "8":
            print("HAVE A GOOD DAY!")
            break
        case _:
            print("Invalid Choice")