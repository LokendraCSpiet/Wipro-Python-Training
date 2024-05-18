#Program to accept the number from the user and calculate sum of digits of a no.
n =int(input("Enter the number to find sum of digits: "))
sum = 0
while n>0:          # 0 > 0
    rem = n%10      # rem = 7%10=7
    sum = sum+rem   # sum = 14
    n=n//10         # n = 0
print("Sum of digits is: ",sum)


'''---------------------------------------------------------------------------
Program to accept the number from the user and calculate the sum of first
and last digit of a number -
Input: 7821
Output: 8 
'''
n = int(input("Enter the number to find sum of first and last digit: ")) # 892
last = n%10                           # last=2
n = n//10                             # n = 89
 
while n>9:                            # 8>9
    n=n//10                           # n = 8
print("Sum of first and last digit is: ",last + n)



'''---------------------------------------------------------------------------
Program to accept the number from the user and calculate sum of digits except
the last digit. if last digit of a number is equal to sum of digits then print
"Wipro" otherwise print "Training"
 
Input: 1236
Output : Wipro
 
Input: 7659
Output: Training
'''
n =int(input("Enter the number to sum of digits except the last digit is last: "))
lastVal = n%10
n //= 10

sum = 0
while n>0:
    sum += n%10
    n=n//10

if lastVal == sum:
    print("Wipro") 
else:
    print("Training")



'''---------------------------------------------------------------------------
Program to check whether the number is a spy number or not
Hint : sum of digits = product of digits
Input: 1124
Output: Spy number
'''

n =int(input("Enter the number to check spy number: "))
sum = 0
multi = 1
while n>0:
    rem = n%10
    sum = sum+rem
    multi = multi * rem
    n=n//10
if sum == multi:
    print("Spy Number")
else:
    print("Not a Spy Number")
   


'''---------------------------------------------------------------------------
Program to check whether the number is automorphic number or not
Hint: Last digits of square of a number is equal to number itself
 
Input: 6
Output: Automorphic number
 
Input: 25
Output: Automorphic number
 
Input: 11
Output: Not an Automophic number
'''
n= int(input("Enter the number to check automorphic: "))    # n = 11
sq = n*n                              # sq = 121
flag = True
while n>0:           #11>0
    if n%10 == sq%10:
        n=n//10      #n==1
        sq=sq//10    #sq=12
    else:
        flag = False
        print("It is not an automorphic number ")
        break
if flag:
    print("It is an automorphic number ")


'''---------------------------------------------------------------------------
Program to count the number of zero , odd and even digits from the number
Input: 10352
Output: Zero = 1 , Odd = 3 , Even = 1
'''

# n =int(input("Enter the number "))
n = 10352
evenCount = 0
oddCount = 0
zeroCount = 0
while n > 0:
    rem = n%10
    if rem == 0:
        zeroCount += 1
    elif rem % 2 == 0:
        evenCount += 1
    else:
        oddCount += 1
    n=n//10

print(f"Zero = {zeroCount} , Odd = {oddCount} , Even = {evenCount}")