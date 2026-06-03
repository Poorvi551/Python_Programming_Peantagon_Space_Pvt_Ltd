# WAP to check whether the given number is armstrong number or not
def armstrong_num(n):
    sum=0
    for i in str(n):
        num=int(i)
        sum=sum+num**len(str(n))
    if sum==n:
        return 'armstrong number'
    else:
        return 'not an armstrong number'
n=int(input("Enter val:"))
print(armstrong_num(n))
