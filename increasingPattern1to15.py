'''
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15
'''


# n=int(input("enter rows"))
# k=1
# i=0
# while(i<n):
#     j=0
#     while(j<i+1):
#         print(k,end=" ")
#         j+=1
#         k+=1
#     print()
#     i+=1


n=int(input("enter rows"))
k=1
for i in range(n):
    for j in range(i+1):
        print(k,end=" ")
        k+=1
    print()

