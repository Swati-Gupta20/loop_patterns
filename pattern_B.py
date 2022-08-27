for i in range(7):
    for j in range(4):
        if (j==0 and (i>0 or i<7))or(j==3 and(i==1 or i==2 or i==4 or i==5))or((j==1 or j==2)and(i==0 or i==3 or i==6)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()