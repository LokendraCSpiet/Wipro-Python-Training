# Method 1:
a = [10, 10, 10, 5, 10, 10, 100, 10, 40, 5, 0, 0]
# a = ['c', 'c', 'c', 'b', 'c', 'c', 'd', 'c', 'g', 'b', 'a', 'a']
a.sort()
num = 0.1
b = []
for i in a:
    if i != num and a.count(i) > 1:
            for j in range(a.count(i)):
                b.append(i)
    num = i
print(b)


# Method 2:
# a = [10, 10, 10, 5, 10, 10, 100, 10, 40, 5, 0, 0]
# output = []
# for key,val in {i:a.count(i) for i in a}.items():
#     if val > 1:
#         for i in range(val):
#             output.append(key)
# print(output)


# Method 3:
# a = [10, 10, 10, 5, 10, 10, 100, 10, 40, 5, 0, 0]
# temp = a[0]
# output = []
# for i in a:
#     if temp != i:
#         temp = i
#     for j in a:

    # for j in a:

# for i in range(len(a)):
#     for j in range(len(a)):


