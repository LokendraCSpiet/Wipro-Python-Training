"""
Write a python program to accept “n” from the user and store it in the list
and display the length of the highest consecutive sequence.
Input:
n = 11
l = [ 1 , 12 , 3 , 4 , 5  , 11 , 2 , 13 , 14 , 15 , 6 ]
 
Output:
Length of highest consecutive sequence is 6
Note: The elements of the list can be either in sorted or unsorted order.
"""

l = [ ]
n = int(input("Enter the number of elements "))
for i in range(n):
    l.append(int(input("Enter the element ")))
# l = [ 1 , 4, 2 , 3 , 11 , 12 , 13 ,14, 15]

l.sort( )
m=0
cnt = 1
for i in range(len(l)-1):
    if l[i] == l[i+1]-1:
        cnt = cnt + 1
    else:
        if cnt > m:
            m = cnt
            cnt = 1
if cnt>m:
    m = cnt
print("The lenght of the highest consecutive sequence is ",m)