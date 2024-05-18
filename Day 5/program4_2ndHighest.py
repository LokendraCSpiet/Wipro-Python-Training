'''
Accept the n elements from the user and store it in the list and display
the 2nd Highest element from the list
'''

l = []
 
n = int(input("Enter the number of elements: "))
 
for i in range(n):
    l.append(int(input("Enter the element: ")))
 
print(l)
l = set(l)
print(l)
l = list(l)
l.sort(reverse= True)
print(l[1])