n=4
for i in range(1,n+1):
    x=n*i
    for j in range(1,n+1):
        print(x,end=" ")
        x-=1
    print()
