def palindrome(n):
    rev=0
    temp=n
    while temp>0:
        ld=temp%10
        rev=rev*10+ld
        temp=temp//10
    if n==rev:
        return 'palindrome'
    else:
        return 'not a palindrome'
n=int(input("Enter num:"))
print(palindrome(n))
