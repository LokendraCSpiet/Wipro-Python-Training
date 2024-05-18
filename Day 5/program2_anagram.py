'''
Program to accept 2 strings from the user and check whether the 2 strings
are anagram or not
 
Hint:
Tried and Tired
heart and earth
fried and fired
ab and ba
'''

s1 = input("Enter the string 1 ").lower()
s2 = input("Enter the string 2 ").lower()
if len(s1)==len(s2):
    if set(s1) == set(s2):
        print("It is anagram ")
    else:
        print("It is not anagram")
 
if sorted(s1) == sorted(s2):
    print("It is anagram ")
else:
    print("It is not an anagram ")