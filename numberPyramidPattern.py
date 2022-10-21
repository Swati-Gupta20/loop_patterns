
'''
          1 
        2 1 2 
      3 2 1 2 3 
    4 3 2 1 2 3 4 
  5 4 3 2 1 2 3 4 5
  '''



# n=int(input("enter rows:-"))
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print(i-j+1,end=" ")
#     for j in range(i+1):
#         print(j+1,end=" ")
#     print()



i=1
while i<=5:
    k=1
    while k<=5-i:
        print(' ',end=' ')
        k+=1
    j=1
    while j<=i:
        print(i-j+1,end=' ')
        j+=1
    i+=1
    print()