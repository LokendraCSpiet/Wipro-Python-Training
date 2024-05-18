"""
Create a base class Account (Acc_Holder_Name, Acc_Holder_Contact_No).
 
Derive a two classes as Saving_Account(S_Acc_No., Balance) and Current_Account( C_Acc_No., Balance) from Account.
 
Write a menu driven program to perform the following functions:
 
1) Accept the details for 'n' saving account holders. 
2) display the details of 'n' saving account holders. 
3) Display the account details whose account balance is less than 10000 for saving account
4) Accept the details for 'n' current account holders. 
5) display the details of 'n' current account holders. 
6) Display the account details whose account balance is less than 5000 for current account
"""
class Account:
    def __init__(self,name,contact):
        self.name = name
        self.contact = contact
 
class SavingAccount(Account):
    def __init__(self,name , contact ,acno, bal):
        super().__init__(name,contact)
        self.acno = acno
        self.bal = bal
 
    def display(self):
        print(f"Name: {self.name}\n  Account no.- {self.acno}\n  Balance- {self.bal} ")

 
class CurrentAccount(Account):
    def __init__(self,name , contact ,acno, bal):
        super().__init__(name,contact)
        self.acno = acno
        self.bal = bal

    def display(self):
        print(f"Name is {self.name}\nAccount no. is {self.acno}\nBalance is {self.bal}")
        print("---")
 
SA = []
CA = []
while True:
    print("---------------------------------------------------------------------------")
    print("(1): Accept details of saving account")
    print("(2): Display details of saving account")
    print("(3): Display the details of saving account whose balance is less than 10000")
    print("(4): Accept details of current account")
    print("(5): Display details of current account")
    print("(6): Display the details of current account whose balance is less than 5000")
    ch = int(input("Enter your choice: "))
    print("---------------------------------------------------------------------------")
    match ch:
        case 1:
            print("Enter Details for Saving Account -")
            name = input("Enter name: ")
            contact = input("Enter contact number: ")
            acno = input("Enter account number: ")
            bal = int(input("Enter the balance: "))
            obj = SavingAccount(name,contact,acno,bal)
            SA.append(obj)
        case 2:
            print("Details of Saving Account -")
            for i in SA:
                i.display()
        case 3:
            print("Display the details of saving account whose balance is less than 10000 -")
            for i in SA:
                if int(i.bal) < 10000:
                    i.display()
        case 4:
            print("Enter Details for Current Account -")
            name = input("Enter name: ")
            contact = input("Enter contact number: ")
            acno = input("Enter account number: ")
            bal = int(input("Enter the balance: "))
            obj = CurrentAccount(name,contact,acno,bal)
            CA.append(obj)
        case 5:
            print("Details of Current Account -")
            for i in CA:
                i.display()
        case 6:
            print("Display the details of Current Account whose balance is less than 5000 -")
            for i in CA:
                if int(i.bal) < 5000:
                    i.display()
        case 7:
            break
        case _:
            print("Invalid Choice")
    input("\nPress Enter to go to menu")






