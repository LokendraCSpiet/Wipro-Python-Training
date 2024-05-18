#Program to check whether the number is prime or not.
n = int(input("Enter the number to check prime: "))
flag = True
for i in range(2,n//2+1):
    if n%i==0:
        print ("It is not a prime number ")
        flag = False
        break
if flag:
    print("It is a prime number ")


#Program to check whether the number is Perfect or not.
n = int(input("Enter the number to check perfect: "))
sum = 0
for i in range(1,n//2+1):
    if n%i==0:
        sum += i
if sum == n:
    print("It is a perfect number ")
else:
    print("It is not a perfect number ")