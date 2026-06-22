n=5
for i in range(1,n+1):
    x=n-i+1
    for j in range(1,n-i+2):
        print(x,end=" ")
        x=x+1
    print()
