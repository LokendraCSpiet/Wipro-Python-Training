input = ['a','a','b','b','b','b','b','c','c']
check = input[0]
count = 0

n = len(input)
for i in range(n):
    if check == input[i]:
        count += 1
    else:
        input.append(check)
        input.append(str(count))
        check = input[i]
        count = 1
    if i+1 == n:
        input.append(check)
        input.append(str(count))


for k in range(n):
    input.remove(input[0])
print(input)