'''
Program to accept 3 political parties name and store it in the dictionary
with the intial value as 0. Accept "n" number of voters from the user
for voting and display the name of winning party. if there is a tie between
the parties display the name of the political parties.
'''
 
parties = { }
 
i=1
while i<=3:
    pname = input("Enter the party name ")
    if pname not in parties.keys():
        parties[pname] = 0
        i = i + 1
    else:
        print("Party name is already present ")
 
i=1
n = int(input("Enter the number of voters "))
while i<=n:
    pname = input("Enter the name of party you want to vote : ")
    if pname in parties.keys( ):
        parties[pname] = parties[pname] + 1
        i = i+1
    else:
        print("Party name is not present ")
 
l = parties.values()
m = max(l)
cnt = 0
s = ""
 
for k,v in parties.items( ):
    if v == m:
        s = s + k + " "
        cnt = cnt + 1
 
if cnt==1:
    print("Winning party is ",s)
else:
    print("There is a tie between ",s)