'''
Write a program to accept the details of Employee from the user. Accept Eid,
Ename , Age , Sal ,Aadhar card no. and pan card no.
 
Validate ename , aadhar card no and pan card no.
- ename should consists of 3 words and all 3 words should consists of alphabets
- aadhar card no. should be of 12 digits
- pan card no [CEHPM4323K]
 
'''
import validate
# from validate import *
 
eid = input("Enter Employee Id: ")
 
while True:
    name = input("Enter Employee name: ")
    if validate.isvalidname(name):
        break
    else:
        print("Name is not valid ")

while True:
    Aadhar = input("Enter Aadhar card no.:")
    if validate.isvalidaadhar(Aadhar):
        break
    else:
        print("Please enter valid aadhar card number")

age = int(input("Enter the Age: "))
sal = int(input("Enter the salary: "))

while True:
    pan = input("Enter Pan card no.: ")
    if validate.isvalidpan(pan):
        break
    else:
        print("Invalid pan card no.")
 
print(f"Name is: {name}\nAadhar no is: {Aadhar}\nPan no is: {pan}")