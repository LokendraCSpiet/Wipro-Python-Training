'''
Write a program to define a user defined function RemoveDuplicateWords( ). The function should return the string after removing all duplicate words from the string.
'''
def RemoveDuplicateWords(inputStr):
    # Method 1:
    uniqueList = []
    words = inputStr.lower().split(" ")
    for i in words:
        if i.lower() not in uniqueList:
            uniqueList.append(i)
    uniqueString = " ".join(list(uniqueList))
    return uniqueString

    # Method 2:
    # uniqueSet = set()
    # words = inputStr.split(" ")
    # for i in words:
    #     uniqueSet.add(i)
    # uniqueString = " ".join(list(uniqueSet))
    # return uniqueString

def remove_duplicates(string1):
    temp = string1.lower().split()
    res=" ".join(dict.fromkeys(temp))
    return res

inputStr = "Hello My name is lokendra, hello what is your name"
inputStr = input("Enter Sentence to remove duplicate words: ")
print(RemoveDuplicateWords(inputStr))

