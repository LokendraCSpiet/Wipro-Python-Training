'''
3. Word Frequency Calculation
Write a function word_frequency that takes a string text as input and returns a dictionary where the keys are unique words in the text, and the values are the frequencies of those words in the text. Treat uppercase and lowercase letters as equivalent.
 
Task
Given a string text, calculate the frequency of each word in the text.
 
Input Format
    Read text, a string representing the text.
 
Constraints
    The length of the text will be at most 10^3.
 
Output Format
    The function must return a dictionary where the keys are unique words in the text and the values are the frequencies of those words.
 
Input   : "Hello world hello"
Output  : {'hello': 2, 'world': 1}
 
Test Cases:
"Hello world hello" = {'hello': 2, 'world': 1}
"Python is awesome, isn't it?" = {'python': 1, 'is': 1, 'awesome': 1, "isn't": 1, 'it': 1}
"Programming is fun Python programming is awesome" = {'programming': 2, 'is': 2, 'fun': 1, 'python': 1, 'awesome': 1}
'''

def reverse_words(sentence):
    sen_list = []
    for i in sentence.lower().split(" "):
        if "?" in i:
            sen_list.append(i.replace("?",""))
        elif "," in i:
            sen_list.append(i.replace(",",""))
        else:
           sen_list.append(i)
    return {I:sen_list.count(I) for I in sen_list}

def main():
    failed_list = []
    count = 0
    total = 3
    if reverse_words("Hello world hello") == {'hello': 2, 'world': 1}:
      count += 1
    else:
      failed_list.append("'Hello world hello'")
    
    if reverse_words("Python is awesome, isn't it?") == {'python': 1, 'is': 1, 'awesome': 1, "isn't": 1, 'it': 1}:
      count += 1
    else:
      failed_list.append("'Python is awesome, isn't it?'")
    
    if reverse_words("Programming is fun Python programming is awesome") == {'programming': 2, 'is': 2, 'fun': 1, 'python': 1, 'awesome': 1}:
      count += 1
    else:
      failed_list.append("'Programming is fun Python programming is awesome'")
    
    print(f"Total Cases: {total}")
    print(f"Passed Cases: {count}")
    print(f"Failed Cases: {total-count}")
    if total-count > 0:
      print(f"Failed For: {', '.join(failed_list)}")
  
if __name__=="__main__":
    main()