'''---------------------------------------------------------------------------
Write a menu driven program to perform the following operations
1) check whether the number is palindrome or not
2) Accept the number from the user and display the sum of even digits and odd digits from a number
    Example:    193024
                Sum of odd digit is 13
                Sum of even digit is 6
3) Program to accept the number of rows and print the following pattern:
    1 2 3
    1 2
    1
4) Exit
'''

while True:
    print("\n1:Palindrome number\n2:Calculating sum of odd and even digits\n3:Pattern\n4:Exit\n")
    ch = input("Enter your choice ")
    match ch:
        case "1":
            n = int(input("enter your number "))
            temp = n
            rev = 0
            while n>0:
                rem =n%10
                rev = rev*10 + rem
                n=n//10
            if rev == temp:
                print("Palindrome number ")
            else:
                print("Not a palindrome number ")
        case "2":
            even=odd=0
            n = int(input("Enter the number "))
            while n>0:
                rem = n%10
                if rem%2==0:
                    even = even + rem
                else:
                    odd = odd + rem
                n=n//10
            print("Odd sum is ",odd)
            print("Even sum is ",even)
 
        case "3":
            n = int(input("Enter the number of rows "))
            for i in range(n,0,-1):
                for j in range(1,i+1):
                    print(j,end=" ")
                print( )
 
        case "4":
            break
        case _:
            print("Invalid choice ")