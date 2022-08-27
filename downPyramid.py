#   * * * * * * * * * 
#     * * * * * * * 
#       * * * * * 
#         * * * 
#           * 




# n=int(input("enter how many rows you want:-"))
# sign=input("enter sign:-")
# for i in range(n):
#     for j in range(i+1):
#        print(" ",end=" ")
#     for j in range(i,n):
#        print(sign,end=" ")   
#     for j in range(i,n-1):
#         print(sign,end=" ")    
#     print()


# whilelop:-
n=int(input("enter rows:-"))
i=0
while(i<n):
   j=0
   while(j<i+1):
      print(" ",end=" ")
      j+=1
   k=0
   while(k<(n-1)-i):
      print("*",end=" ")
      k+=1
   a=0
   while(a<n-i):
      print("*",end=" ")
      a+=1
   print()
   i+=1