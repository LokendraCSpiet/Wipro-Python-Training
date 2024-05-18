#Copy the contents of 1 file into another file
try:
    file1 = input("Enter the name of the file for reading the data ")
    fr = open(file1)
 
    file2 = input("Enter the name of the file for writting the data ")
    fw = open(file2,"w")
 
    for i in fr.read():
        fw.write(i)
    fr.close()
    fw.close()
except:
    print("File is not present ")


# Method 2 : with open -
#Copy the contents of 1 file into another file
try:
    file1 = input("Enter the name of the file for reading the data ")
    file2 = input("Enter the name of the file for writting the data ")
    with open(file1) as fr:
        with open (file2,"w") as fw:
            for i in fr.read():
                fw.write(i)
except:
    print("File is not present ")