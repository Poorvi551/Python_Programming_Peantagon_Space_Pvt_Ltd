# WAP to swap numbers without using temporary variable
def swap_without_temp(n1,n2):
    n1,n2=n2,n1
    return n1,n2
n1=int(input("Enter num1:"))
n2=int(input("Enter num2:"))
print(swap_without_temp(n1,n2))
