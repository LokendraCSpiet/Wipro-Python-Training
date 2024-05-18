
# Arbitary positinal argument
def fun(*b):
    s=0
    for i in b:
        s = s+i
    print(s)
 
fun(10,20,30,40)



# Arbitary keyword argument
def fun2(**b):
    for i,j in b.items():
        print(f"{i} = {j}")

fun2(a=21,b="Lok",c=81.67)