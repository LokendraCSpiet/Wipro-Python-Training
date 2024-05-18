"""
Program to accept the number from the user and check whether the number is
magic number or not.[Define a user define function sumofdigits(n) which will
return the sum of digits of a number]
 
Hint: Sum of digit till it reduces to single digit and a single digit is 1
then it is a magic number
"""


def sumofdigits(n):
    sum = 0
    while n>0:
        sum += n%10
        n //= 10
    return sum

n = int(input("Enter the number to check magic number: "))
while n > 9:
    n = sumofdigits(n)
if n == 1:
    print("Magic number ")
else:
    print("It is not a magic number ")