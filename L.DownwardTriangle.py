'''
 1 1 1 1 1 
   2 2 2 2 
     3 3 3 
       4 4 
         5 '''


# n=int(input("enter rows:-"))
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print(i+1,end=" ")
#     print()



# while loop:-
n=int(input("enter rows:-"))
i=0
while(i<n):
    j=0
    while(j<=i):
        print(" ",end=" ")
        j+=1
    k=0
    while(k<n-i):
        print(i+1,end=" ")
        k+=1
    i+=1
    print()
