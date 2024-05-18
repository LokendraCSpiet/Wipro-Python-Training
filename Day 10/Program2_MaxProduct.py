'''
Maximum Product of Two Integers :
Write a function max_product that takes a list of integers nums as input and 
returns the maximum product that can be obtained by multiplying two distinct integers from the list.
 
Task:
Given a list of integers nums, find the maximum product that can be obtained by 
multiplying two distinct integers from the list.
 
Input Format
    Read nums, a list of integers.
 
Constraints
    The length of the list nums will be at most 10^3.
    Each element in the list nums will be an integer in the range [-1000, 1000].

Output Format
    The function must return an integer representing the maximum product of two distinct integers 
    from the input list.
 
Input  : [1, 2, 3, 4, 5]
Output : 20 [The maximum product is obtained by multiplying 5 and 4 (5 * 4 = 20)]
 
Test Cases
[1, 2, 3, 4, 5] = 20
[-10, -3, 5, 2, -7] = 70
[0, -1, -2, -3]	= 6
'''

def maximum_product(input_list):
  product = 1
  for i in range(0,len(input_list)):
      for j in range(i+1,len(input_list)):
          multi = input_list[i] * input_list[j]
          if multi > product:
              product = multi
  return product

def main():
  failed_list = []
  count = 0
  total = 3
  
  if maximum_product([1, 2, 3, 4, 5]) == 20:
    count += 1
  else:
    failed_list.append("[1, 2, 3, 4, 5]")

  if maximum_product([-10, -3, 5, 2, -7]) == 70:
    count += 1
  else:
    failed_list.append("[-10, -3, 5, 2, -7]")

  if maximum_product([0, -1, -2, -3]) == 6:
    count += 1
  else:
    failed_list.append("[0, -1, -2, -3]")

  print(f"Total Cases: {total}")
  print(f"Passed Cases: {count}")
  print(f"Failed Cases: {total-count}")
  if total-count > 0:
    print(f"Failed For: {', '.join(failed_list)}")
  
if __name__=="__main__":
  main()