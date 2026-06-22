# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n or j==1 or j==n:
#             print("*",end=" ")
#         elif j==3:         # or j=n//2+1
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# or

n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n or j==n//2+1:
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()