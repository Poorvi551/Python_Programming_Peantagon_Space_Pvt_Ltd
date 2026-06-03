# wAP to check whether the given the number is perfect number or not
def perfect_num(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    if sum==n:
        return 'perfect number'
    else:
        return 'not a perfect number'
n=int(input("Enter num:"))
print(perfect_num(n))
