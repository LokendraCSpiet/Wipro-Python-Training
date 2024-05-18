"""
Write a program to find uncommon words from the two strings
Input:
String 1: Welcome all of you to Wipro
String 2: Welcome all of you in python session
Output:
to Wipro in python session
"""

str1 = input("Enter the string 1: ").lower().split()
str2 = input("Enter the string 2: ").lower().split()
unmatch1 = []
unmatch2 = []
l = min(len(str1),len(str2))
for i in range (l):
    if str1[i] != str2[i]:
        unmatch1.append(str1[i])
        unmatch2.append(str2[i])
value = unmatch1 + unmatch2
difflen = abs(len(str1)-len(str2))
diff_str = min(str1,str2)
for j in range(l,l+difflen):
    value.append(diff_str[j])
output = " ".join(value)
print(output)


# Method 1:
l1 = input("Enter the string 1: ").lower().split()
l2 = input("Enter the string 2: ").lower().split()
for i in l1:
    if i not in l2:
        print(i,end=" ")
for i in l2:
    if i not in l1:
        print(i,end=" ")
 
# Method 2:
l1 = input("Enter the string 1: ").lower().split()
l2 = input("Enter the string 2: ").lower().split()
 
s1 = set(l1)
s2 = set(l2)
 
s3 = s1.intersection(s2)

s4 =s1-s3
s5 =s2-s3
print(s4,s5)