'''
a = 10
b = 20
if a == b:
    break
else:
    print("pass")
 
 
for i in range(1,10,2):
    match i:
        case 5:
            print("Hello",end=" ")
 
        case 1:
            print("Hi",end=" ")
 
        case 7:
            break
 
        case _:
            print("!!",end=" ")
 
 
x = "Wipro","Python","session"
print(x[1][2:4])
 
l= ["AA","BB"]
for i in l:
    i.lower()
print(l)
 
 
l = ["AA","BB"]
for i in range(2):
    i.lower()
print(l)
 
 
i = 1
while i<=10:
    print(i)
    if i==3:
        continue
    i=i+1
 
 
i = 1
while i<=10:
    print(i)
    if i==5:
        break
    i=i+1
    print(i)
 
#1 2 2 3 3 4 4 5 5
 
'''