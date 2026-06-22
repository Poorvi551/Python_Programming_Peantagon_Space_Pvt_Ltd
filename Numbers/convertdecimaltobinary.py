# WAP to convert decimal to binary
def convert_binary(n):
    bin=''
    while n>0:
        r=n%2
        bin=str(r)+bin
        n=n//2
    return bin
n=int(input("Enter num:"))
print(convert_binary(n))

