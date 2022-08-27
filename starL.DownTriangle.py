'''
 * * * * *
   * * * * 
     * * * 
       * * 
         *
'''
n=int(input("enter rows:-"))
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    print()



# while loop:-
# n=int(input("enter rows:-"))
# i=0
# while(i<n):
#     j=0
#     while(j<=i):
#         print(" ",end=" ")
#         j+=1
#     k=0
#     while(k<n-i):
#         print("*",end=" ")
#         k+=1
#     i+=1
#     print()