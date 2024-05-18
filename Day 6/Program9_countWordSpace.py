"""
Program to read the contents of the file "Wipro.txt" and count the number
of words and spaces in the file.
"""

try:
    # file1 = input("Enter the name of the file for reading the data ")
    # file2 = input("Enter the name of the file for writting the data ")
    file = "wipro.txt"
    countStr = 0  
    # countNum = 0  
    countSpace = 0  
    with open(file) as fr:
        for i in fr.read():
            if i.isspace():
                countSpace += 1
            elif i.isalpha():
                countStr += 1
            # elif i.isdigit():
            #     countNum += 1
except IOError:
    print("File is not present ")

print(f"Number of Words: {countStr}, Space: {countSpace}")


# By Sir -
try:
    with open("wipro.txt") as fr:
        words = 0
        spaces = 0
        for i in fr.readlines():
            words = words + len(i.split())
            spaces= spaces + len(i.split())-1
        print("Number of words: ",words)
        print("Number of spaces: ",spaces)
except :
    print("File is not present")