# n=4
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j%2==0:
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#     print()

    #OR

n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        print((j+1)%2,end=" ")
    print()