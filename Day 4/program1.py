""" 
Automorphic, 
sum of digit of no., 
palindrome, 
disarium 
"""


while True:
    ch = input("Program by the String Method -\n1.Automorphic\n2.sum of digit of no.\n3.palindrome\n4.disarium\nEnter your choice:")
    match ch:
        case "1":
            n = input("enter your number ")
            square = str(int(n)*int(n))
            if square.endswith(n):
                print("Automorphic")
            else:
                print("Not Automorphic")
        
        case "2":
            n = input("Enter a number:")
            sum = 0
            for i in n:
                sum += int(i)
            print("Sum of digits is:",sum)
        
        case "3":
            n = input("Enter a number:")
            if n == n[::-1]:
                print("Palindrome number")
            else:
                print("Not a palindrome number")
        
        case "4":
            n = input("Enter a number:")
            sum=0
            for i in range(0,len(n)):
                sum += int(n[i])**(i+1) 
            if str(sum) == n:
                print("Disarium number")
            else:
                print("Not a Disarium number")
