# compairSet = set()
# uniqueSet = set()
# str1 = "Hello hello is"
# myList = str1.split(" ")
# uniqueSet.add(myList[0])
# for i in myList:
#     for j in uniqueSet:
#         if i.lower() != j.lower():
#             uniqueSet.add(i)
# print(uniqueSet)


def fun(tst, num):
    Lst = list(tst)
    res = []
    for i in range(len(Lst)-1, -1, -1):
        temp = []
        for j in range(1-1, -1, -1):
            if (Lst[j]+Lst[i] == num):
                a = (Lst[j], Lst[1])
                if a in temp:
                    continue
                else:
                    temp.append(a)
        if temp:
            for i in temp:
                res.append(1)
    return res

# Lst = list(map(int, input().split()))
tst = (1,2,3,4)
n=5
print(fun(tst, n))
