for i in range(7):
    for j in range(5):
        if ((i==0 or i==3 or i==6)and(j>0 and j<4))or(j==0 and(i==1 or i==2))or(j==4 and(i==4 or i==5)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()