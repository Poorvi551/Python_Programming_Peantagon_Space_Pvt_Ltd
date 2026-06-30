#wap to print index values of the given element without using index values. - assignment q2

l=eval(input("Enter list:"))
val=int(input("Enter val:"))
for i in range(len(l)):
    if l[i]==val:
        print(i)
        break

# def find_index_without_idxmetd(l,val):
#     for i in range(len(l)):
#         if l[i]==val:
#             print(i)
#             break
# l=eval(input("Enter list:"))
# val=int(input("Enter val:"))
# find_index_without_idxmetd(l,val)
