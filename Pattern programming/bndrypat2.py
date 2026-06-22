# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n or j==1 or j==n:
#             print("*",end=" ")
#         else:
#             print("+",end=" ")
#     print()



n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("*",end=" ")
        elif i==2 or j==2 or i==4 or j==4:
            print("+",end=" ")
        else:
            print(" ",end=" ")
    print()