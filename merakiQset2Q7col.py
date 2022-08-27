'''
5 4 3 2 1
5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1
 '''


# n= int(input("enter rows:"))
# for i in range(n):
#     for j in range(n):
#         print(n-j,end=" ")
#     print()



n= int(input("enter rows:"))
i=0
while(i<n):
    j=0
    while(j<n):
        print(n-j,end=" ")
        j+=1
    print()
    i+=1