"""
Program to define a function isprime(n) which return True if the number is
prime otherwise it return False. Accept the number from the user and check
whether the number is twisted prime or not.
"""


def isprime(n):
    for i in range(2,n//2+1):
        if n%i ==0:
            return False
    return True

n = int(input("Enter the number to check twisted prime: "))
if isprime(n):
    n = str(n)
    n1 = n[::-1]
    n1 = int(n1)
    if isprime(n1):
        print("It is a twisted prime number ")
    else:
        print("It is not a twisted prime number ")
else:
    print("It is not a twisted prime number ")