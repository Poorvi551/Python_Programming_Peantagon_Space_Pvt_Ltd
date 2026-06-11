l1=eval(input("Enter list1:"))
l2=eval(input("Enter list2:"))
if len(l1)==len(l2):
    out={}
    for i in range(len(l1)):
        out[l1[i]]=l2[i]
    print(out)
