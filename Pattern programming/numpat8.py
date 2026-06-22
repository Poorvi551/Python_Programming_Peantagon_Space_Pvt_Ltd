n=5
for i in range(1,n+1):
    for space in range(1,n-i+1):
        print(" ",end=" ")
    x = 1
    for j in range(1,i+1):
        print(x,end=" ")
        x=x+1
    y=i-1
    for k in range(1,i):
        print(y,end=" ")
        y=y-1
    print()
