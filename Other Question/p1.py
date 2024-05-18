"""
1. Write a function that returns True if two arrays, when combined, 
form a consecutive sequence. A consecutive sequence is a sequence without 
any gaps in the integers, e.g. 1, 2, 3, 4, 5 is a consecutive sequence, 
but 1, 2, 4, 5 is not.

input - [7, 4, 5, 1], [2, 3, 6]
input - [2,3,4,5], [6,7,8]
input - [44, 46], [45]
output - True

input - [2,3,4,5],[1,2,3,4,5]
output - False
"""

def consecutive_combo(l1,l2):
    l1.extend(l2)

    check = l1[0]
    flag = True
    for i in range(1,len(l1)):
        if l1[i] - check != 1:
            flag = False
        check = l1[i]

    return flag
# print(consecutive_combo([2,3,4,5],[6,7,8,9]))


"""
2. check if the given string is balance. The string w.ill have only {,},(,),[,} characters
s1 = "{{[]}(){}}"
"""

def is_balanced_1(s1):
    L = list(s1)
    d = {i:L.count(i) for i in L}
    if d['{'] == d['}'] and d['('] == d[')'] and d['['] == d[']']:
        return True
    else:
        return False
    
def is_balanced_2(s):
    stack = []  # {
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():  # }
            if not stack or mapping[char] != stack.pop():
                return False
            
        else:
            return False
    return not stack
    
def is_balanced_3(s):
    while '{}' in s or '()' in s or '[]' in s:
        s = s.replace('{}', '').replace('()', '').replace('[]', '')
    return not s

s1 = "{{[]}(){}}"
print(is_balanced_1(s1))
# print(balance_string(s1))
# print(is_balanced(s1))


"""
3. Find the highest sum of adjacent numbers in the below list
list1 = [8,-6,9,3,12,7,4]
"""




"""
4 if a number is perfect if all digits of the number is a factor of the given number
Find the numbers which are perfect in the range 2,48
"""
