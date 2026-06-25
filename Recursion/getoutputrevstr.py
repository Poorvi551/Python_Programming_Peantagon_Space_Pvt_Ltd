def sam(l,out=[],i=0):
    if i>=len(l):
        return out
    if type(l[i])==str:
        out.append(l[i][::-1]+l[i])
    else:
        out.append(l[i])
    return sam(l,out,i+1)
l=eval(input("Enter list:"))
print(sam(l))