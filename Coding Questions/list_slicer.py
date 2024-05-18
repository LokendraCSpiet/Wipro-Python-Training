def list_slicer(input_list, n):
    """
    :param input_list: List from which elements are to be sliced.
    :param n: The slice step, to take every nth element.
    :return: A list containing every nth element.
    """
    if n <= 0:
        print("Slice step 'n' should be a positive integer")
        # raise ValueError("Slice step 'n' should be a positive integer")
    else:
        # Method 1:
        # sliced_list = []
        # for eachVal in range(0,len(input_list),n):
        #     sliced_list.append(input_list[eachVal])
        # print(sliced_list)
        # return sliced_list

        # Method 2:
        return [input_list[eachVal] for eachVal in range(0,len(input_list),n)]





''' --------------------------- For Check Test Cases --------------------------- '''
total = 7
count = 0
failed_list = []

# test_every_second_element    
if list_slicer([1, 'a', 2, 'b', 3, 'c'], 2) == [1, 2, 3]:
    count += 1
else:
    failed_list.append("test_every_second_element")


# test_every_third_element    
if list_slicer([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == [1, 4, 7]:
    count += 1
else:
    failed_list.append("test_every_third_element")


# test_with_empty_list    
if list_slicer([], 3) == []:
    count += 1
else:
    failed_list.append("test_with_empty_list")


# test_with_single_element    
if list_slicer(['a'], 1) == ['a']:
    count += 1
else:
    failed_list.append("test_with_single_element")


# test_with_varied_data_types    
if list_slicer(['a', 1, None, True, 'b', 3.14], 2) == ['a', None, 'b']:
    count += 1
else:
    failed_list.append("test_with_varied_data_types")


# test_with_nonexistent_nth_element    
if list_slicer([1, 2, 3], 5) == [1]:
    count += 1
else:
    failed_list.append("test_with_nonexistent_nth_element")


# test_with_step_zero  
if list_slicer([1, 2, 3], 0) == None:
    count += 1
else:
    failed_list.append("test_with_step_zero")


print(f"Total Cases: {total}")
print(f"Passed Cases: {count}")
print(f"Failed Cases: {total-count}")
if total-count > 0:
    print(f"Failed For: {', '.join(failed_list)}")



""" 
from app.list_slicer import list_slicer
import pytest


def test_every_second_element():
    assert list_slicer([1, 'a', 2, 'b', 3, 'c'], 2) == [1, 2, 3]

def test_every_third_element():
    assert list_slicer([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == [1, 4, 7]

def test_with_empty_list():
    assert list_slicer([], 3) == []

def test_with_single_element():
    assert list_slicer(['a'], 1) == ['a']

def test_with_varied_data_types():
    assert list_slicer(['a', 1, None, True, 'b', 3.14], 2) == ['a', None, 'b']

def test_with_nonexistent_nth_element():
    assert list_slicer([1, 2, 3], 5) == [1]

def test_with_step_zero():
    with pytest.raises(ValueError):
        list_slicer([1, 2, 3], 0)
"""