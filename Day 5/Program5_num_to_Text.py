""" 
Write a python program to accept the number from the user and print the
number in words.
Input: 1401
Output: One Four Zero One
"""

valList = []
l = ['zero','one','two','three','four','five','six','seven','eight','nine']
n = input("Enter the number ")
for i in n:
    # print(l[int(i)],end=" ")
    valList.append(l[int(i)])
value = " ".join(valList)
print(value)