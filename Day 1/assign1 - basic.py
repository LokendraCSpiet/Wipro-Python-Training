'''
1.Program to find maximum of 2 numbers
2.Program to find minimum of 3 numbers
3.Program to accept the number from the user and check whether number is even or odd
4.Program to accpet the  number and check whether it is positive or negative
'''

# Program to find maximum of 2 numbers - 
num1 = int(input("Enter Number 1 for find maximum:"))
num2 = int(input("Enter Number 2 for find maximum:"))
if num1 == num2:
    print("Both The Number are same")
elif num1 > num2:
    print("The Number 1 is Maximum")
else:
    print("The Number 2 is Maximum")


# Program to find minimum of 3 numbers -
num1 = int(input("Enter Number 1 for find minimum:"))
num2 = int(input("Enter Number 2 for find minimum:"))
num3 = int(input("Enter Number 3 for find minimum:"))

if (num1 < num2) and (num1 < num3):
    sm_num = num1
elif (num2 < num1) and (num2 < num3):
    sm_num = num2
else:
    sm_num = num3
print("The smallest is: ", sm_num)


# Program to accept the number from the user and check whether number is even or odd - 
number = int(input("Enter Number to check even or odd:"))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Program to accpet the  number and check whether it is positive or negative -
num = int(input("Enter number to check positive or negative:"))
if num == 0:
    print("Zero")
elif num > 0:
    print("Positive")
else:
    print("Negitive")