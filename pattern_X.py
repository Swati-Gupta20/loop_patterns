# n=7
# for i in range(n):
#     for j in range(n):
#         if (i==j or i+j==n-1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

n=9
i=0
while(i<n):
    j=0
    while(j<n):
        if (i==j or i+j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j+=1
    print()
    i+=1