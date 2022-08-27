'''
Q. Dcreasing Triangle:-

*   *   *   *   *
*   *   *   *
*   *   *
*   *
*
'''

# n=int(input("enter a no."))
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print("*",end=" ")
#     print()


# OR

# i=1
# while(i<=5):
#     print("* "*i)
#     i+=1

# # OR

# n=int(input("enter a no."))
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print()




'''
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1'''


# n=int(input("enter rows"))
# i=0
# while(i<n):
#     j=0
#     while(j<n-i):
#         print(n-i,end=" ")
#         j+=1
#     print()
#     i+=1

# for loop:-
n=int(input("enter a no."))
for i in range(n):
    for j in range(n-i):
        print(n-i,end=" ")
    print()