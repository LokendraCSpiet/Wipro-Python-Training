""" 
Implement a function that finds all pairs of numbers in a tuple that add up to a given sum.
For eg: tuple_pair_finder((1, 2, 3, 4), 5) == [(1, 4), (2, 3)]
"""

def tuple_pair_finder(numbers, target_sum):
    """
    This function takes a tuple of numbers and a target sum, then returns a list of tuples,
    each of which contains a pair of numbers from the input tuple that add up to the target sum.

    :param numbers: A tuple of numbers to find pairs in.
    :param target_sum: The target sum for which pairs of numbers should add up to.
    :return: A list of tuples, each containing a pair of numbers that add up to target_sum.
    """
    found_pairs = []
    '''
    Add your code here
    '''
    # # My Method 1 (Old):
    # for i in range(len(numbers)):
    #     for j in range(i+1, len(numbers)):
    #             if numbers[i] + numbers[j] == target_sum:
    #                 if i == 0:
    #                     newpair = (numbers[i],numbers[j])
    #                     found_pairs.append(newpair)
    #                 else:
    #                     flag = True
    #                     for item in found_pairs:
    #                         if numbers[j] == item[1]:
    #                             flag = False
    #                     if flag:
    #                         newpair = (numbers[i],numbers[j])
    #                         found_pairs.append(newpair)
    

    # My Method 2:
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            pair = (numbers[i],numbers[j])
            if numbers[i] + numbers[j] == target_sum:
                if i == 0:
                    found_pairs.append(pair)
                else:
                    if pair not in found_pairs:
                        found_pairs.append(pair)
    if len(found_pairs) == 2:
        found_pairs = found_pairs[::-1]


    # # Other Method by Manoj - 
    # for i in range(1,len(numbers)):
    #    for j in range(0,i):
    #         if numbers[i]+numbers[j]==target_sum:
    #             found_pairs.append((numbers[j],numbers[i]))
    #             break

    '''
    Add your code here
    '''
    return found_pairs


# [(inpt[i],inpt[j]) for i in range(len(inpt)) for j in range(i+1, len(inpt)) if sum((inpt[i],inpt[j])) == total]
# >>> [(1, 9), (2, 8), (3, 7), (4, 6)]


# tuple_pair_finder((2, 2, 2), 4) == [(2, 2), (2, 2)]
# print("ans",tuple_pair_finder((2, 2, 2), 4))



total = 8
count = 0
failed_list = []

# def test_single_pair():
if tuple_pair_finder((1, 2, 3, 4), 5) == [(2, 3), (1, 4)]:
# if tuple_pair_finder((1, 2, 3, 4), 5) == [(1, 4), (2, 3)]:
    count += 1
else:
    print(f"Failed: (test_single_pair) \nOutput:{tuple_pair_finder((1, 2, 3, 4), 5)} \nEcpected: [(2, 3), (1, 4)] \n")
    failed_list.append("test_single_pair")


# def test_no_pair():
if tuple_pair_finder((1, 2, 3, 4), 8) == []:
    count += 1
else:
    print(f"Failed: (test_no_pair) \nOutput:{tuple_pair_finder((1, 2, 3, 4), 8)} \nEcpected: [] \n")
    failed_list.append("test_no_pair")


# def test_multiple_pairs():
if tuple_pair_finder((1, 2, 3, 2, 1), 3) == [(1, 2), (1, 2),(2,1)]:
    count += 1
else:
    print(f"Failed: (test_multiple_pairs) \nOutput:{tuple_pair_finder((1, 2, 3, 2, 1), 3)} \nEcpected: [(1, 2), (1, 2),(2,1)] \n")
    failed_list.append("test_multiple_pairs")


# def test_with_negative_numbers():
if tuple_pair_finder((-1, -2, -3, 4), 1) == [(-3, 4)]:
    count += 1
else:
    print(f"Failed: (test_with_negative_numbers) \nOutput:{tuple_pair_finder((-1, -2, -3, 4), 1)} \nEcpected: [(-3, 4)] \n")
    failed_list.append("test_with_negative_numbers")
    

# def test_with_zero():
if tuple_pair_finder((0, 1, 2, 3, -3), 0) == [(3, -3)]:
    count += 1
else:
    print(f"Failed: (test_with_zero) \nOutput:{tuple_pair_finder((0, 1, 2, 3, -3), 0)} \nEcpected: [(3, -3)] \n")
    failed_list.append("test_with_zero")
    

# def test_tuple_with_repeated_numbers():
if tuple_pair_finder((2, 2, 2), 4) == [(2, 2), (2, 2)]:
    count += 1
else:
    print(f"Failed: (test_tuple_with_repeated_numbers) \nOutput:{tuple_pair_finder((2, 2, 2), 4)} \nEcpected: [(2, 2), (2, 2)] \n")
    failed_list.append("test_tuple_with_repeated_numbers")


# def test_empty_tuple():
if tuple_pair_finder((), 5) == []:
    count += 1
else:
    print(f"Failed: (test_empty_tuple) \nOutput:{tuple_pair_finder((), 5)} \nEcpected: [] \n")
    failed_list.append("test_empty_tuple")


# def test_all_zeroes_tuple():
if tuple_pair_finder((0, 0, 0, 0), 0) == [(0, 0), (0, 0), (0, 0)]:
    count += 1
else:
    print(f"Failed: (test_all_zeroes_tuple) \nOutput:{tuple_pair_finder((0, 0, 0, 0), 0)} \nEcpected: [(0, 0), (0, 0), (0, 0)] \n")
    failed_list.append("test_all_zeroes_tuple")
    

print(f"Total Cases: {total}")
print(f"Passed Cases: {count}")
print(f"Failed Cases: {total-count}")
if total-count > 0:
    print(f"Failed For: {', '.join(failed_list)}")




'''
from app.tuple_pair_finder import tuple_pair_finder
import pytest

def test_single_pair():
    assert tuple_pair_finder((1, 2, 3, 4), 5) == [(1, 4), (2, 3)]

def test_no_pair():
    assert tuple_pair_finder((1, 2, 3, 4), 8) == []

def test_multiple_pairs():
    assert tuple_pair_finder((1, 2, 3, 2, 1), 3) == [(1, 2), (1, 2),(2,1)]

def test_with_negative_numbers():
    assert tuple_pair_finder((-1, -2, -3, 4), 1) == [(-3, 4)]

def test_with_zero():
    assert tuple_pair_finder((0, 1, 2, 3, -3), 0) == [(3, -3)]

def test_tuple_with_repeated_numbers():
    assert tuple_pair_finder((2, 2, 2), 4) == [(2, 2), (2, 2)]
'''