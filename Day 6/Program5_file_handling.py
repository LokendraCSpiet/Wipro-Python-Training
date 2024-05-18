try:
    f = open("wipro.txt")
    '''
    Functions used to read the data from the file
    for i in f.read():
        print(i)

 
    print(f.readline()) # It will read a single line
    print(f.readlines()[1])
    '''    
except:
    print("File is not present ")

print("Thank You")


# Methods - 
""" 
import os
os.rename("yasir.txt","manoj.txt")
os.remove("kavya.txt")
"""