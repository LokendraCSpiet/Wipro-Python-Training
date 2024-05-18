# n = 3
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print("")

# n = 3
# for i in range(1,n+1):
#     for j in range(n,i-1,-1):
#         print(j,end=" ")
#     print("")

'''---------------------------------------------------------------------------
program to print the following pattern for n lines
1 2 3
1 2
1
'''
n =int(input('''To print the following pattern -
1 2 3
1 2
1 
Enter the number: '''))
# n =int(input("Enter the number:"))
for i in range (n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("")


'''---------------------------------------------------------------------------
program to print the following pattern for n lines
3
3 2
3 2 1
'''
n =int(input('''To print the following pattern -
3
3 2
3 2 1 
Enter the number: '''))
for i in range (n,0,-1):
    for j in range(n,i-1,-1):
        print(j,end=" ")
    print("")


'''---------------------------------------------------------------------------
program to print the following pattern for n lines
1
1 0
1 0 1
1 0 1 0
'''
n =int(input('''To print the following pattern -
1
1 0
1 0 1
1 0 1 0
Enter the number: '''))
for i in range(1,n+1):
    for j in range(1,i+1):
        # if j%2==0:
        #     num = 0
        # else:
        #     num = 1
        # print(num,end=" ")
        print(j%2,end=" ")
    print("")


'''--------------------------------------------------------------------------- 
program to print the following pattern for n lines
* * * *
*     *
*     *
* * * *
'''
n =int(input('''To print the following pattern -
* * * *
*     *
*     *
* * * *
Enter the number: '''))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("* ",end="")
        else:
            print("  ",end="")
    print()


'''---------------------------------------------------------------------------
program to print the following pattern for n lines
    *
  * *
* * *
'''
n =int(input('''To print the following pattern -
    *
  * *
* * *
Enter the number: '''))
for i in range(1,n+1):
    print("  " * (n-i),end="")
    print("* " * i)


'''---------------------------------------------------------------------------
program to print the following pattern for n lines
  * 
 * *
* * *
'''
n =int(input('''To print the following pattern -
  * 
 * *
* * *
Enter the number: '''))
for i in range(1,n+1):
    print(" " * (n-i),end="")
    print("* " * i)