'''
          * 
        * * 
      * * * 
    * * * * 
  * * * * *'''


# n=int(input("enter rows:-"))
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()


# while loop:-
# n=int(input("enter rows:-"))
# i=0
# while(i<n):
#     j=0
#     while(j<n-i):
#         print(" ",end=" ")
#         j+=1
#     k=0
#     while(k<=i):
#         print("*",end=" ")
#         k+=1
#     print()
#     i+=1



'''  
        1    
      1 2  
    1 2 3 
  1 2 3 4 
1 2 3 4 5
'''
# n=int(input("enter rows:-"))
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i+1):
#       print(j+1,end=" ")
#     print()


# whileloop:-
n=int(input("enter rows:-"))
i=0
while(i<n):
  j=0
  while(j<n-i):
    print(" ",end=" ")
    j+=1
  k=0
  while(k<=i):
    print(k+1,end=" ")
    k+=1
  i+=1
  print()
