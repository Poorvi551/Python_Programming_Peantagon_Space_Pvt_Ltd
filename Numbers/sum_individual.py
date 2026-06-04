#WAP to find the sum of the individual digit
def sum_individual(n):
    sum=0
    while n>0:
        ld=n%10
        sum=sum+ld
        n=n//10
    return sum
n=int(input("Enter num:"))
print(sum_individual(n))