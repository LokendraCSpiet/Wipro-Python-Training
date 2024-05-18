'''---------------------------------------------------------------------------
Write a menu driven program to perform the following operations on the string.
1)Check whether the number is pronic number or not
    Hint: Pronic number is the number which is the product of two consecutive integers.
    Examples:   12 = 3 * 4
                20 = 4 * 5
                42 = 6 * 7
2)Check whether the number is a Niven number or not.
    Niven number: A number is said to be Niven which is divisible by the sum of its digits.
    Example:    126
                Sum of its digits = 1 + 2 + 6 = 9 and 126 is divisible by 9.
3)Check whether the number is Armstrong number or not.
    Armstrong number: A number is said to be Armstrong if sum of cube of each digit is equal to number
    Example:    153
                1 + 125 + 27 = 153
4)Exit
'''

while True:
    print("\n1:Pronic number\n2:Niven number\n3:Armstrong number\n4:Exit\n")
    ch = input("Enter your choice ")
    match ch:
        case "1":
            n = int(input("Enter the number "))
            flag = True
            for i in range(1,n//2+1):
                if i * (i+1) == n:
                    flag = False
                    print("It is pronic number ")
                    break
            if flag:
                print("It is not a pronic number")
        case "2":
            n = int(input("Enter the number "))
            temp =n
            sum = 0
            while n>0:
                sum = sum + n%10
                n = n//10
            if temp%sum == 0:
                print("Niven number ")
            else:
                print("It is not a niven number ")
 
        case "3":
            n = int(input("Enter the number "))
            temp = n
            sum = 0
            while n>0:
                rem = n%10
                sum = sum + (rem**3)
                n=n//10
            if temp == sum:
                print("It is armstrong number ")
            else:
                print("It is not an armstrong number ")
        case "4":
            break
        case _:
            print("Invalid choice ")