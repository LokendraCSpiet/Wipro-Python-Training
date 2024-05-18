'''
Write a Python program to define a user defined function ispangram( ). The function should return if the string is pangram otherwise return False.
Hint:
    A pangram is a sentence containing every letter in the English Alphabet.
    Input: The quick brown fox jumps over the lazy dog
    Output: The given string is pangram
'''

def ispangram(inputStr):
    uniqueSet = set()
    for i in inputStr:
        if i.isalpha():
            uniqueSet.add(i.lower())
    if len(uniqueSet) == 26:
        return "The given string is pangram"
    else:
        return False
    
    # Method 2:
    temp = list(inputStr.lower())
    res = list(dict.fromkeys(temp))
    if len(res)-1 == 26:
        return True
    else:
        return False
    

inputStr = "The quick brown fox jumps, over the lazy dog."
inputStr = input("Enter santance to check pangram: ")
print(ispangram(inputStr))

