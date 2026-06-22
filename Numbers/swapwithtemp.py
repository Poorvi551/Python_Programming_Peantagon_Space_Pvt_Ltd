# WAP to swap two numbers using temporary variable
# def swap_using_temp(n1,n2):
#     temp=n1
#     for i in n1,n2:
#         if temp==n1:
#             temp=n2
#         else:
#             temp=n1
#     return temp
# n1=int(input("Enter n1:"))
# n2=int(input("Enter n2:"))
# print(swap_using_temp(n1,n2))


def swap_using_temp(n1,n2):
    temp=n1
    n1=n2
    n2=temp
    return n1,n2
n1=int(input("Enter n1:"))
n2=int(input("Enter n2:"))
print(swap_using_temp(n1,n2))
