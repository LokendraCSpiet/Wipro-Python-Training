'''
Reversing Words in a Sentence
Write a function reverse_words that takes a string sentence as input and 
returns a string where the order of words in the sentence is reversed. 
You may assume that words are separated by a single space and 
that there are no leading or trailing spaces in the input string.
 
Task
Given a string sentence, reverse the order of words in the sentence.
 
Input Format
    Read sentence, a string representing the sentence.
  Constraints
    The sentence will contain at most 10^3 characters.

Output Format
    The function must return a string representing the reversed order of words in the input sentence.

Sample Input  : "hello world"
Sample Output : "world hello"
 
Explanation : The words "hello" and "world" are reversed in the sentence.
 
Test Cases 
Input	                            Expected Output
"hello world"	                    "world hello"
"python is awesome"	                "awesome is python"
"coding challenges are fun"	        "fun are challenges coding"
'''

def reverse_words(sentence):
  return " ".join(sentence.split(" ")[::-1])

def main():
  failed_list = []
  count = 0
  total = 3
  if reverse_words("hello world") == "world hello":
    count += 1
  else:
    failed_list.append("hello worlds")

  if reverse_words("python is awesome") == "awesome is python":
    count += 1
  else:
    failed_list.append("python is awesome")

  if reverse_words("coding challenges are fun") == "fun are challenges coding":
    count += 1
  else:
    failed_list.append("coding challenges are fun")

  print(f"Total Cases: {total}")
  print(f"Passed Cases: {count}")
  print(f"Failed Cases: {total-count}")
  if total-count > 0:
    print(f"Failed For: {', '.join(failed_list)}")
  
if __name__=="__main__":
  main()