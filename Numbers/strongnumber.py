#WAP to check whether a given number is astrong number or not
def strong_number(n):
    sum=0
    for i in str(n):
        num=int(i)
        fact=1
        for j in range(1,num+1):
            fact=fact*j
        sum=sum+fact
    if sum==n:
        return 'Strong number'
    else:
        return 'Not a strong number'
n=int(input("Enter num:"))
print(strong_number(n))

