'''
1
4 9
16 25 36
49 64 81 100
'''


n=int(input("enter rows:-"))
i=1
e=1
while(i<n):
    j=1
    while(j<=i):
        print(e**2,end=" ")
        j+=1
        e=e+1
    print()
    i+=1


# forloop:-

# n=int(input("enter rows:-"))
# e=1
# for i in range(n):
#     for j in range(i+1):
#         print(e**2,end=" ")
#         e+=1
#     print()

