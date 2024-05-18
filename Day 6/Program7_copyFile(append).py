#Copy the contents of 1 file into another file
try:
    file1 = input("Enter the name of the file for reading the data ")
    file2 = input("Enter the name of the file for writting the data ")
    with open(file1) as fr:
        with open (file2,"a") as fw:
            for i in fr.read():
                fw.write(i)
except IOError:
    print("File is not present ")