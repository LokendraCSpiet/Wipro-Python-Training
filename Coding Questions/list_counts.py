def unique_element_counter(numbers):
    output_dict = {}
    for i in numbers:
        if i not in output_dict:
            output_dict[i] = 1
        else:
            output_dict[i] += 1
    
    return output_dict

# list1 = [1,2,3,1,5,4,2,3,1,2,4,3,1,2,1]
# print(unique_element_counter(list1))


''' --------------------------- For Check Test Cases --------------------------- '''
total = 4
count = 0
failed_list = []


# test_with_duplicates
if unique_element_counter([1, 2, 2, 3, 3, 3]) == {1: 1, 2: 2, 3: 3}:
    count += 1
else:
    failed_list.append("test_with_duplicates")

# test_with_empty_list
if unique_element_counter([]) == {}:
    count += 1
else:
    failed_list.append("test_with_empty_list")

# test_with_single_element
if unique_element_counter(['single']) == {'single': 1}:
    count += 1
else:
    failed_list.append("test_with_single_element")

# test_with_no_duplicates
if unique_element_counter([1, 2, 3]) == {1: 1, 2: 1, 3: 1}:
    count += 1
else:
    failed_list.append("test_with_no_duplicates")


print(f"Total Cases: {total}")
print(f"Passed Cases: {count}")
print(f"Failed Cases: {total-count}")
if total-count > 0:
    print(f"Failed For: {', '.join(failed_list)}")


"""  
import unittest

from app.element_counter import unique_element_counter
# Test cases for the unique_element_counter function

def test_with_duplicates():
    assert unique_element_counter([1, 2, 2, 3, 3, 3]) == {1: 1, 2: 2, 3: 3}

def test_with_empty_list():
    assert unique_element_counter([]) == {}

def test_with_single_element():
    assert unique_element_counter(['single']) == {'single': 1}

def test_with_no_duplicates():
    assert unique_element_counter([1, 2, 3]) == {1: 1, 2: 1, 3: 1}
"""






# dict1 = {1: 5, 2: 4, 3: 3, 5: 1, 4: 2}


# newIt = list(dict1)
# newIt.sort()

# newDict = dict(newIt)
# print(newDict)
# # print(list(dict1).sort())
# # print(list(dict1))

