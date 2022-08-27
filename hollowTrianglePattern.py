# i=0
# while(i<5):
#     j=0
#     while(j<9):
#         if (i==0 and j==4)or(i==1 and(j==3 or j==5))or(i==2 and (j==2 or j==6))or(i==3 and (j==1 or j==7))or((j>=0 or j<=8)and i==4) :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#         j+=1
#     i+=1
#     print()

# for loop:-

for i in range(5):
    for j in range(9):
        if (i==0 and j==4)or(i==1 and(j==3 or j==5))or(i==2 and (j==2 or j==6))or(i==3 and (j==1 or j==7))or((j>=0 or j<=8)and i==4) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
