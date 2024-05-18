'''
Program to accept the number from the user and check whether number is unique
number or not
 
Hint:
Each digit should be repeated only once.
1034 - unique number
10341 - Not a unique number
 
'''

n =input("Enter the number:")
if len(n) == len(set(n)):
    print("It is unique number")
else:
    print("It is not a unique number")