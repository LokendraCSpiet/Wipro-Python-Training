 
# 1. What is the maximum possible length of an identifier?
# 32
# 64
# 128
# No fixed length is specified


# 2. Which character is used in Python to make a single line comment?
# @
# $
# %
# #


# 3. Which of the following declarations is incorrect?
# _X = 2
# _X_ = 2
# __X = 10
# None of the mentioned


# 4. Which of the following statements is correct for variable names in Python language?
# All variable names must begin with an underscore.
# Unlimited length
# The variable name length is a maximum of 2.
# All of the above


# 5. what is the output of the following code:
# x = ['XX', 'YY']  
# for i in x:  
#     i.lower()  
# print(x)  
# ['XX', 'YY']
# ['xx', 'yy']
# ['XX' , 'yy' ]
# ['xx' , 'YY']


# 6. Trace the output:
# i = 1:  
# while True:  
#     if i%3 == 0:  
#         break  
#     print(i,end=" ") 
# 1 2 3
# 1
# 3 2 1
# Invalid syntax
 
 
# 7. Trace the output:
# i = 0  
# while i < 5:  
#     print(i,end=" ")  
#     i += 1  
#     if i == 3:  
#         break  
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4
# Syntax Error
 

# 8. Trace the output:
# z = "xyz"  
# j = "j"  
# while j in z:  
#     print(j, end=" ")  
# xyz
# It will print j infinite times
# x y z
# No output
 
 
# 9. Trace the output:
# x = 'pqrs'  
# for i in range(len(x)):  
#     x[i].upper()  
# print (x)   
# PQRS
# pqrs
# PQrs
# Error
 

# 10. Trace the output:
# def abbrev(first_name, last_name):
#    print(first_name[0:1] + ". " + last_name.lower())
# abbrev("Joanne", "Weathers")
# J.weathers
# J.Weathers
# Jo.weathers
# Jo.Weathers
 

# 11. After running this code, what would be the output if the input was first_name = "Katie" and last_name = "perkins"?
# def abbrev():
#    first_name = input("What is your first name? ")
#    last_name = input("What is your last name? ")
#    return("Hello " + first_name + last_name[0:2].capitalize() + ". ")
# def main():
#    abbrev()
# main()
# Hello KatiePe.
# Hello Katie Pe.
# Hello Katie PE.
# Nothing will be get printed
 
 
# 12. Given the variable item, how would you grab the letters “tebo”?
# def notebook():
#    item = "notebook"
#    # What goes here?
# notebook()
# print(item[2:7])
# print(item[2:6])
# print(item[-2:-7])
# print(item[3:7])
 

# 13. Suppose list1 is [1, 5, '9'], what is sum(list1)?
# 15
# 1
# 9
# Error
 
 
# 14. d = {"john":40, "peter":45}
# "john" in d
# True
# False
# None
# Error
 

# 15. Trace the output:
# x = 'abcd'
# for i in range(len(x)):
#     print(i,end=" ")
# a b c d
# 0 1 2 3
# 1 2 3 4
# Error
 

# 16. Trace the output:
# x = 'abcd'
# for i in range(len(x)):
#     print(i.upper(),end=" ")
# A B C D
# a b c d
# 0 1 2 3
# Error
 
 
# 17. Trace the output:
# x = 'abcd'
# for i in range(len(x)):
#     x[i].upper()
# print (x,end="")
# ABCD
# Error
# abcd
# None of the mentioned
 

# 18. Which of the following function is not a valid function for list
# pop( )
# remove( )
# pop(index)
# del(index)
 
 
# 19. Trace the output:
# myList = [1, 5, 5, 5, 5, 1]
# max = myList[0]
# indexOfMax = 0
# for i in range(1, len(myList)):
#     if myList[i] > max:
#         max = myList[i]
#         indexOfMax = i
# print(indexOfMax)
# 1
# 2
# 3
# 4
 

# 20. Trace the output:
# myList = [1, 2, 3, 4, 5, 6]
# for i in range(1, 6):
#     myList[i - 1] = myList[i]
# for i in range(0, 6):
#     print(myList[i], end = " ")
# 2 3 4 5 6 6
# 2 3 4 5 6 1
# 1 1 2 3 4 5
# 6 1 2 3 4 5
 

# 21. Trace the output
# a = 10
# b = 20
# if a == b:
#     break
# else:
#     print("Not Equal")
# print("Pass")
# Pass
# No output
# Not Equal
# Error
 
 
# 22. Trace the output
# for i in range(1,10,2):
#     match i:
#         case 1:
#             print("Hi ", end="")
#         case 5:
#             print("Hello ",end="")
#         case 7:
#             break
#         case _:
#             print("!! ",end="")
# Hi !! Hello
# Hi Hello !!
# Hi Hello !! !!
# Error
 

# 23. Trace the output
# for i in range(1,10):
#     if 2%i!=0:
#         print(i,end=" ")
# 3 4 5 6 7 8 9
# 1 2
# 1 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8
 

# 24. Trace the output
# i=1
# while i<=20:
#     print(i,end=" ")
#     i=i+2
#     if i==9:
#         continue
#     print(i,end=" ")
#     if i==11:
#         break;
# 1 3 3 5 5 7 7 9 11
# 1 3 3 5 5 7 7 9 11 11
# 1 3 5 5 7 7 9 11
# 1 3 3 5 7 7 9 11
 

# 25. Trace the output
# for i in range(20,10,-12):
#     print(i)
# 20
# 20 8
# Infinite loop
# Error



# By sir --- 
# a = 10
# b = 20

# while True:
#     if a != b:
#         continue
#     a = a - 1
#     print(a)
#     if a == 5:
#         break