        #   * 
#         * * * 
#       * * * * * 
#     * * * * * * * 
#   * * * * * * * * *




# n=int(input("enter how many rows you want:-"))
# for i in range(n):
#     for j in range(i,n):
#        print(" ",end=" ")
#     for j in range(i):
#        print("*",end=" ")
#     for j in range(i+1):
#        print("*",end=" ")
#     print()

# whileloop:-



# n=int(input("enter rows:-"))
# i=0
# while(i<n):
#    j=0
#    while(j<n-i):
#       print(" ",end=" ")
#       j+=1
#    k=0
#    while(k<i+1):
#       print("*",end=" ")
#       k+=1
#    a=0
#    while(a<i):
#       print("*",end=" ")
#       a+=1
#    print()
#    i+=1

# short code:-
n=5
a=0
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(a+1):
        print("*",end=" ")
    print()
    a+=2