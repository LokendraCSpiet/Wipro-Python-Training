"""
Create a class Bank Account with following details:
Account Number, Account Holder name, Age, Type of Account, Balance, Pan Card number.
1. Create Account
2. Delete Account
3. Deposit
4. Withdraw
5. Funds Transfer
6. Search details of account holder
    a. Search by account number
    b. Search by Type of Account
7. Balance Enquiry
"""
class bank_account:
    def __init__(self, account_number, account_Holder_name, age, account_type, balance, pan_card_number):
        self.account_number = account_number
        self.account_Holder_name = account_Holder_name
        self.age = age
        self.account_type = account_type
        self.balance = int(balance)
        self.pan_card_number = pan_card_number
        
    def display(self):
        print("Account Number = {}, Account Holder name = {}, Age = {}, Type of Account = {}, Balance = {}, Pan Card number = {}".format(
            self.account_number,
            self.account_Holder_name,
            self.age,
            self.account_type,
            self.balance,
            self.pan_card_number
        ))

acc_details = []
while True:
    print("----------------------------------------")
    print("(1) Create Account")
    print("(2) Delete Account")
    print("(3) Deposit")
    print("(4) Withdraw")
    print("(5) Funds Transfer")
    print("(6) Search details of account holder")
    print("(7) Balance Enquiry")
    print("(8) Display")
    print("(9) Exit")
    ch = int(input("Enter Your Choice: "))
    print("----------------------------------------")
    match ch:
        case 1:
            print("Create Account")
            account_number = input("Enter Account Number: ")
            account_Holder_name = input("Enter Account Holder Name: ")
            age = input("Enter Age: ")
            account_type = input("Enter Type of Account: ")
            balance = input("Enter Balance: ")
            pan_card_number = input("Enter Pan Card Number: ")
            obj = bank_account(account_number, account_Holder_name, age, account_type, balance, pan_card_number)
            acc_details.append(obj)
        case 2:
            print("Delete Account")
            accNo = input("Enter Account Number: ")
            flag = True
            for i in acc_details:
                if i.account_number == accNo:
                    acc_details.remove(i)
                    flag = False
            if flag:
                print("Account Not Found")
        case 3:
            # Case Diposit
            print("Case Diposit")
            amountDeposit = int(input("Enter Deposit Amount: "))
            accNo = input("Enter Account Number: ")
            flag = True
            for i in acc_details:
                if i.account_number == accNo:
                    i.balance += amountDeposit
                    flag = False
            if flag:
                print("Account Not Found")
        case 4:
            # Case Withdral
            print("Case Withdral")
            amount_withdraw = int(input("Enter Withdraw Amount: "))
            accNo = input("Enter Account Number: ")
            flag = True
            for i in acc_details:
                if i.account_number == accNo:
                    i.balance -= amount_withdraw
                    flag = False
            if flag:
                print("Account Not Found")
        case 5:
            # Funds Transfer
            print("Funds Transfer")
            accNo = input("Enter Sender's Account Number: ")
            selfflag = True
            transflag = True
            for i in acc_details:
                if i.account_number == accNo:
                    selfflag = False
                    amount = int(input("Enter Amount: "))
                    if amount < i.balance:
                        accNo2 = input("Enter Receiver's Account Number: ")
                        for j in acc_details:
                            if j.account_number == accNo2:
                                transflag = False
                                i.balance -= amount
                                j.balance += amount
                    else:
                        print("Insufficient Balance")
            if selfflag:
                print("Sender's Account Not Found")
            else:
                if transflag:
                    print("Receiver's Account Not Found")
        case 6:
            # Search details of account holder
            print("Search details of account holder")
            print("(A) Search by account number")
            print("(B) Search by Type of Account")
            ch2 = input("Enter Your Choice: ").upper()
            match ch2:
                case "A":
                    accNo = input("Enter Your Account Number: ")
                    for i in acc_details:
                        if i.account_number == accNo:
                            i.display()
                        else:
                            print("Your Account Not Found")
                case "B":
                    accType = input("Enter Type of Account: ")
                    for i in acc_details:
                        if i.account_type == accType:
                            i.display()
                        else:
                            print("This Type of Account Not Found")
                case _:
                    print("Invalid Choice")
        case 7:
            # Balance Enquiry
            print("Balance Enquiry")
            accNo = input("Enter Your Account Number: ")
            for i in acc_details:
                if i.account_number == accNo:
                    print("Your Balance is: ",i.balance)
                    i.display()
                else:
                    print("Your Account Not Found")
        case 8:
            print("Display")
            for i in acc_details:
                i.display()
        case 9:
            break
        case _:
            print("Invalid Choice")
