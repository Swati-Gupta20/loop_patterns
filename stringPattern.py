'''
c
c o
c o d
c o d e
c o d e r
'''

# str=input("enter any word:-")
# len=len(str)
# i=0
# while(i<len):
#     j=0
#     while(j<i+1):
#         print(str[j],end=" ")
#         j+=1
#     print()
#     i+=1


# forloop:-
str=input("enter any word:-")
len=len(str)
for i in range(len):
    for j in range(i+1):
        print(str[j],end=" ")
    print()

