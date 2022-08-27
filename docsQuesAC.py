'''
A 
B C 
D E F
G H I J  '''


n=int(input("enter rows:-"))
p=65
i=0
while(i<n):
    j=0
    while(j<=i):
        print(chr(p),end=" ")
        j+=1
        p+=1
    print()
    i+=1


# for loop:-

# n=int(input("enter rows:-"))
# p=65
# for i in range(n):
#     for j in range(i+1):
#         print(chr(p),end=" ")
#         p+=1
#     print()







