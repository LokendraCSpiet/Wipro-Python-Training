# Program to find the maximum of 2 numbers and also calcualte the sum
 
import sys
 
if len(sys.argv) ==3:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    if a == b:
        print("Values are same ")
    elif a>b:
        print(f"{a} is max ")
    else:
        print(f"{b} is max")
    print(f"Addition is {a+b}")
else:
    print("number of arguments should be 2 ")


# Run - (run on Console)
# [lokendraarya@lokendra Day 5]$ python sys_program.py 10 20