d = {101:"Aliasger" , 102:"Ganesh", 103:"Mukul" ,104:"Ibrahim"}
 
print(len(d))
 
print(d.values())
 
print(d.keys())
 
# How to add and modify the value in the dictionary
d[105] = "Keerthan" # if the key is not present then it will add the element
print(d)
 
d[101] = "Mohan" # if the key is present then it will update the value
print(d)
 
#How to delete the element from the dictionary
del d[103]
print(d)
 
d.pop(102)
print(d)
 
# Fetching the elements of dictionary
for k,v in d.items():
    print(k," = ",v)