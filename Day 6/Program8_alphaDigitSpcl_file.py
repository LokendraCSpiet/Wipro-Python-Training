"""
Program to read the contents of the file "Wipro.txt" and write all alphabets
in alpha.txt , digits in digit.txt and special character in spcl.txt [Dont
include space in the special character]
"""
# import re
try:
    file = "wipro.txt"
    file1 = "alpha.txt"
    file2 = "digit.txt"
    file3 = "spcl.txt"
    with open(file) as fr:
        for i in fr.read():
            if i.isalpha():
                with open (file1,"a") as fw:
                    fw.write(i)
            elif i.isdigit():
                with open (file2,"a") as fw:
                    fw.write(i)
            else:
                if not i.isspace():
                    with open (file3,"a") as fw:
                        fw.write(i)
            # if re.match(r'[^a-zA-Z0-9\s]', i):
            #     with open (file3,"a") as fw:
            #         fw.write(i)
except:
    print("File is not present ")


""" 
# By sir - 
try:
    fr = open("Wipro.txt")
    fa = open("alpha.txt","w")
    fd = open("digit.txt","w")
    fs = open("spcl.txt","w")
    for i in fr.read( ):
 
        if i.isalpha( ):
            fa.write(i)
        elif i.isdigit( ):
            fd.write(i)
        elif not i.isspace( ):
            fs.write(i)
    fa.close()
    fd.close()
    fs.close()
    fr.close()
except:
    print("file is not present ") 
"""