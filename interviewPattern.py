'''
1 
1 2 1 
1 2 3 2 1 
1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1
'''


# n=int(input("enter rows:-"))
# i=0
# while(i<n):
#     j=0
#     while(j<i+1):
#         print(j+1,end=" ")
#         j+=1
#     k=0
#     while(k<i):
#         print(i-k,end=" ")
#         k+=1
#     print()
#     i+=1


n=int(input("enter rows:-"))
for i in range(n):
    for j in range(n-i):
        print(' ',end=' ')
    for j in range(i+1):
        print(j+1,end=" ")
    for j in range(i):
        print(i-j,end=" ")
    print()




    