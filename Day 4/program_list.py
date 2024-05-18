'''
# ------------------------------------------------------------------------------
Write a program to accept the string from the user and display the lenght of
each word
 
Input:
Welcome to training session
 
Output:
welcome = 7
to = 2
training = 8
session = 7
'''
s = "welcome to training session"
# s = input("Enter a string to check length of each:")
s = s.split()
for i in s:
    print(i," = ",len(i))

'''
# ------------------------------------------------------------------------------
Write a program to print the palindrome words from the string
Input:Welcome madam to aba classes
Output:
madam aba
'''
s = "Welcome madam to aba classes"
# s = input("Enter a string to check length of each:")
s = s.split()
out = ""
for i in s:
    if i == i[::-1]:
        out += i+" "
print(out)


'''
# ------------------------------------------------------------------------------
Write a program to accept the string from the user and print the following pattern
 
Input: Hello
Output:
H
He
Hel
Hell
Hello
'''
s = "Hello"
# s = input("Enter a string to check length of each:")
for i in range(1,len(s)+1):
    print(s[0:i])



'''
------------------------------------------------------------------------------
Accept the string from the user and print the word with highest length
 
Input: Welcome to session in wipro
Output: Welcome Session
'''
s = "Welcome to session in wipro"
# s = input("Enter a string to check length of each:")
s = s.split()
lenHigh = 0
highest = []
out = ""
for i in s:
    if len(i)>=lenHigh:
        lenHigh = len(i)
        highest.append(i)
for j in highest:
    out += j+" "
print(out)

